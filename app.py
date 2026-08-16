import streamlit as st
from pathlib import Path
import sys

# Ensure src folder is on Python path
src_dir = Path(__file__).parent / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from coder.crew import Coder

st.set_page_config(
    page_title="CrewAI Coder & Report Generator",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ CrewAI Coder & Report Generator")
st.markdown("Automated agent that writes code, executes inside a Docker sandbox, and generates a formatted Word (`.docx`) report.")

# Assignment prompt input
assignment = st.text_area(
    "Enter Assignment Topic / Problem Statement:",
    value="Demonstrate k-Nearest Neighbor (k-NN) classification on Iris dataset and plot decision boundaries",
    height=120
)

if st.button("🚀 Generate Word Report", type="primary", use_container_width=True):
    if not assignment.strip():
        st.error("Please enter an assignment prompt.")
    else:
        with st.spinner("🤖 Agent is generating code, executing in Docker container, and compiling Word report..."):
            try:
                output_dir = Path(__file__).parent / "output"
                output_dir.mkdir(parents=True, exist_ok=True)
                (output_dir / "assignment.txt").write_text(assignment.strip())

                inputs = {"assignment": assignment.strip()}
                Coder().crew().kickoff(inputs=inputs)

                st.success("✅ Report generated successfully!")

                # Check for output Word doc
                doc_path = output_dir / "solution.docx"
                if not doc_path.exists():
                    doc_path = output_dir / "solution_latest.docx"

                if doc_path.exists():
                    with open(doc_path, "rb") as fp:
                        st.download_button(
                            label="📄 Download solution.docx Report",
                            data=fp.read(),
                            file_name="solution.docx",
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                            use_container_width=True
                        )

                # Show preview images if present
                st.markdown("### Output Previews")
                col1, col2 = st.columns(2)
                term_img = output_dir / "terminal_output.png"
                plot_img = output_dir / "plot.png"

                with col1:
                    if term_img.exists():
                        st.image(str(term_img), caption="Terminal Execution Output")

                with col2:
                    if plot_img.exists():
                        st.image(str(plot_img), caption="Generated Plot/Visualization")

            except Exception as e:
                st.error(f"An error occurred during execution: {e}")
