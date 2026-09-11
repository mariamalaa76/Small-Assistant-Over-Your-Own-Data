from document_processor.loaders.pdf_loader import PDFLoader
from document_processor.loaders.txt_loader import TXTLoader
from document_processor.loaders.rtf_loader import RTFLoader

def print_document_info(file_type, documents):
    print(f"\n--- {file_type} ---")
    print(f"Number of pages: {len(documents)}")
    for i, document in enumerate(documents):
        print(f"Document {i + 1}")
        print(f"Content preview: {document.page_content[:100]}")
        print(f"Metadata: {document.metadata}")
        
        
    
def main():
    pdf_loader = PDFLoader()
    txt_loader = TXTLoader()
    rtf_loader = RTFLoader()

    pdf_documents = pdf_loader.load("data/Mariam_Abdelfattah_CV 3.pdf")
    txt_documents = txt_loader.load("data/AI Engineer job_1.txt")
    txt_documents = txt_loader.load("data/AI Engineer job_2.txt")
    txt_documents = txt_loader.load("data/AI Engineer job_3.txt")
    rtf_documents = rtf_loader.load("data/Study Notes.rtf")

    print(f"PDF: {len(pdf_documents)} pages")
    print(f"TXT: {len(txt_documents)} pages")
    print(f"RTF: {len(rtf_documents)} pages")
    
    print_document_info("PDF", pdf_documents)
    print_document_info("TXT", txt_documents)
    print_document_info("RTF", rtf_documents)


if __name__ == "__main__":
    main()