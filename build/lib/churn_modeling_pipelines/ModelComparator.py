import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display, Markdown

class ModelComparator:
    """
    ModelComparator – Compare Best Variants Across Multiple Models

    Features:
    - Cost-sensitive selection
    - Composite score ranking with printed weights
    - Cleanly separated visualizations
    - Single best model identification
    """

    @staticmethod
    def generate_model_summary(all_model_results):
        """
        Extract best variant from each model based on prioritized ranking:
        - Highest Recall
        - Then Lowest Cost
        - Then Highest F1-Score

        Returns:
            summary_df (DataFrame): A combined table showing the top variant per model
        """
        best_variants = []

        for df in all_model_results:
            df = df.copy()
            df_sorted = df.sort_values(by=["Recall", "Cost ($)", "F1-Score"], ascending=[False, True, False])
            best_variant = df_sorted.iloc[0]
            best_variants.append(best_variant)

        summary_df = pd.DataFrame(best_variants).reset_index(drop=True)

        min_cost = summary_df["Cost ($)"].min()
        summary_df["is_best_cost"] = summary_df["Cost ($)"].apply(
            lambda x: "🟩 True" if x == min_cost else "🟥 False"
        )

        return summary_df

    @staticmethod
    def identify_overall_best_model(summary_df, plot=True):
        """
        Ranks models using a composite score based on weighted metrics:
        - Accuracy, Precision, Recall, F1-Score, and Cost ($)

        Args:
            summary_df (DataFrame): Top variant per model from generate_model_summary
            plot (bool): Whether to render comparative charts

        Returns:
            df (DataFrame): Ranked table with composite scores and visual flags
        """
        df = summary_df.copy()

        weights = {
            'Accuracy': 1.0,
            'Precision': 1.0,
            'Recall': 1.5,
            'F1-Score': 1.5,
            'Cost ($)': 2.0
        }

        for metric in ['Accuracy', 'Precision', 'Recall', 'F1-Score']:
            df[f'n_{metric}'] = (df[metric] - df[metric].min()) / (df[metric].max() - df[metric].min())

        df['n_Cost ($)'] = 1 - (df['Cost ($)'] - df['Cost ($)'].min()) / (df['Cost ($)'].max() - df['Cost ($)'].min())

        df['Composite Score'] = (
            df['n_Accuracy'] * weights['Accuracy'] +
            df['n_Precision'] * weights['Precision'] +
            df['n_Recall'] * weights['Recall'] +
            df['n_F1-Score'] * weights['F1-Score'] +
            df['n_Cost ($)'] * weights['Cost ($)']
        )

        max_score = df['Composite Score'].max()
        df['is_overall_best'] = df['Composite Score'].apply(lambda x: "✅ Best" if x == max_score else "")

        df.drop(columns=[col for col in df.columns if col.startswith('n_')], inplace=True)
        df.sort_values(by="Composite Score", ascending=False, inplace=True)
        df.reset_index(drop=True, inplace=True)

        if plot:
            display(Markdown("## Composite Score by Model"))
            plt.figure(figsize=(10, 5))
            sns.barplot(data=df, x='Model', y='Composite Score', hue='is_overall_best', dodge=False)
            plt.title("Composite Score per Model")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

            display(Markdown("<hr style='border-top: 3px double #bbb;'>"))

            display(Markdown("## 🎯 Accuracy vs Cost ($)"))
            plt.figure(figsize=(10, 6))
            sns.scatterplot(
                data=df,
                x='Cost ($)',
                y='Accuracy',
                hue='Model',
                style='is_overall_best',
                s=150
            )
            plt.title("Accuracy vs Cost for Best Variants")
            plt.tight_layout()
            plt.show()

        return df

    @staticmethod
    def plot_composite_scores_with_labels(df):
        """
        Plots composite scores per model and adds score labels on each bar.
        """
        import matplotlib.pyplot as plt
        import seaborn as sns

        plt.figure(figsize=(10, 5))
        ax = sns.barplot(
            data=df,
            x='Model',
            y='Composite Score',
            hue='is_overall_best',
            dodge=False,
            palette=['#4B73B8' if best == '✅ Best' else '#CC8455' for best in df['is_overall_best']]
        )

        # Annotate each bar with its composite score
        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f'{height:.2f}',
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=10, fontweight='bold')

        plt.title("Composite Score per Model")
        plt.xlabel("Model")
        plt.ylabel("Composite Score")
        plt.xticks(rotation=45)
        plt.legend(title='is_overall_best')
        plt.tight_layout()
        plt.show()

