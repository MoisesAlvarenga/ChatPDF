import streamlit as st
from utils import text

def main():

    st.set_page_config(page_title='CHatPDF', page_icon=':books:')

    with st.sidebar:
        st.subheader('Seus arquivos')
        pdf_docs = st.file_uploader('Carregue os seus arquivos em formato PDF', accept_multiple_files=True)

        if st.button('Processar'):
            all_files_text = text.process_files(pdf_docs)
            print(all_files_text)


if __name__ == '__main__':
    main()