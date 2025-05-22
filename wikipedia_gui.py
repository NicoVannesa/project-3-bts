import wikipediaapi
import gradio as gr

def fetch_summary(topic):
    wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent='project-3-study-app (andromachintoupi@gmail.com)'
    )
    page = wiki.page(topic)
    if not page.exists():
        return "⚠️ Topic not found. Please try another."
    summary = page.summary
    cleaned = " ".join(summary.split()[:500])
    return "📘 " + cleaned

iface = gr.Interface(
    fn=fetch_summary,
    inputs=gr.Textbox(label="Enter a Wikipedia Topic"),
    outputs=gr.Textbox(label="Cleaned Summary"),
    title="📚 Wikipedia Study Summarizer",
    description="Type any academic topic. For best results, use specific terms like 'Quantum Mechanics' instead of vague ones like 'Quantum Theory'."
)

if __name__ == "__main__":
    iface.launch()
