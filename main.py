import streamlit as st
import apinasdata  # Import your scraping function

def main():
    st.title('Nasdaq Scraping App')

    # Button to trigger scraping
    if st.button('Scrape Nasdaq Data'):
        try:
            # Call the scrape_nasdaq function
            apinasdata.scrape_nasdaq()

            # Display success message
            st.success('Scraping completed successfully')
        except Exception as e:
            # Display error message if an exception occurs
            st.error(f'Error: {str(e)}')

if __name__ == '__main__':
    main()
