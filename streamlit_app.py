import streamlit as st


def main():
    st.title('Simple Conversion App')

    conversion_choice = st.radio("Choose Conversion", ['Miles to Kilometers', 'Kilometers to Miles'])

    if conversion_choice == 'Miles to Kilometers':
        miles = st.text_input('Enter miles', value='1.0')
        if st.button('Submit'):
            if miles.replace('.', '', 1).isdigit():
                miles = float(miles)
                kilometers = miles * 1.60934
                st.write(f'{miles} miles is equal to {kilometers} kilometers.')
            else:
                st.write('Please enter a valid number.')
    else:
        kilometers = st.text_input('Enter kilometers', value='1.0')
        if st.button('Submit'):
            if kilometers.replace('.', '', 1).isdigit():
                kilometers = float(kilometers)
                miles = kilometers / 1.60934
                st.write(f'{kilometers} kilometers is equal to {miles} miles.')
            else:
                st.write('Please enter a valid number.')


if __name__ == "__main__":
    main()
