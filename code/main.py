import subprocess
import streamlit as st
import os
import pandas as pd

# Add a logo to the Streamlit app
st.markdown(
    """
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <h1 style="margin: 0;">RegMind - Regulatory Reporting Made Easy</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'processing_done' not in st.session_state:
    st.session_state.processing_done = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = 1

# Function to save uploaded file with a new name and path
def save_uploaded_file(uploaded_file, new_name, new_path):
    try:
        os.makedirs(new_path, exist_ok=True)
        with open(os.path.join(new_path, new_name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return False
    
def run_command():
    # Define the command you want to run in the terminal
    command = "python app.py"
    
    # Run the command in the terminal
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Return the output of the command
    return result.stdout

def paginate_dataframe(df, page_size, page_num):
    start_idx = (page_num - 1) * page_size
    end_idx = start_idx + page_size
    paginated_df = df.iloc[start_idx:end_idx]
    # Replace \n with <br> for HTML rendering
    paginated_df = paginated_df.applymap(lambda x: x.replace('\n', '<br>') if isinstance(x, str) else x)
    return paginated_df

# Progress stepper
st.markdown(f"### Step {st.session_state.step} of 4")
st.progress(st.session_state.step / 4)

# Step 1: Upload Instructions
if st.session_state.step == 1:
    uploaded_file1 = st.file_uploader("Upload Instructions (.txt)", type=["txt"], key="file1")
    if uploaded_file1 is not None:
        if save_uploaded_file(uploaded_file1, "Instruction.txt", "src/resources/dataInput"):
            st.session_state.step = 2
            st.query_params = {"step": 2}

# Step 2: Upload Mock Data
if st.session_state.step == 2:
    uploaded_file2 = st.file_uploader("Upload Mock Data (.csv)", type=["csv"], key="file2")
    if uploaded_file2 is not None:
        if save_uploaded_file(uploaded_file2, "train.csv", "src/resources/dataInput"):
            st.session_state.step = 3
            st.query_params = {"step": 3}

# Step 3: Upload Column Descriptions
if st.session_state.step == 3:
    uploaded_file3 = st.file_uploader("Upload Column Descriptions (.txt)", type=["txt"], key="file3")
    if uploaded_file3 is not None:
        if save_uploaded_file(uploaded_file3, "column_instructions.txt", "src/resources/dataInput"):
            st.session_state.step = 4
            st.query_params = {"step": 4}

# Step 4: Process Data button
if st.session_state.step == 4:
    st.success("All files uploaded successfully!")
    if st.button("Process Data"):
        with st.spinner("Processing..."):
            # Simulate a long-running process
            import time
            time.sleep(3)
            output = run_command()
            # st.write("Progress:")
            # st.code(output)
            st.session_state.processing_done = True

# Display the CSV file in a scrollable table if processing is done
if st.session_state.processing_done:
    csv_file_path = "src/resources/dataOutput/final_anomalies_ui.csv"
    if os.path.exists(csv_file_path):
        df = pd.read_csv(csv_file_path)
        st.write("Anomaly Data:")
        
        # Add download button for the whole anomaly data
        whole_anomaly_data_path = "src/resources/dataOutput/final_anomalies.csv"
        if os.path.exists(whole_anomaly_data_path):
            with open(whole_anomaly_data_path, "rb") as file:
                btn = st.download_button(
                    label="Download Whole Anomaly Data",
                    data=file,
                    file_name="whole_anomaly_data.csv",
                    mime="text/csv"
                )
        else:
            st.error("Whole anomaly data file not found.")
        
        # Pagination
        page_size = 10
        total_pages = (len(df) + page_size - 1) // page_size
        current_page = st.session_state.current_page

        paginated_df = paginate_dataframe(df, page_size, current_page)
        st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
        st.write(paginated_df.to_html(index=False, classes='dataframe-container', escape=False), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Pagination controls
        col1, col2, col3 = st.columns([1, 2, 1])
        if col1.button("Previous"):
            if current_page > 1:
                st.session_state.current_page -= 1
        col2.write(f"Page {current_page} of {total_pages}")
        if col3.button("Next"):
            if current_page < total_pages:
                st.session_state.current_page += 1
    else:
        st.error("CSV file not found.")