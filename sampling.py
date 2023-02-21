import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

def Home():
    st.title("Home") 
    st.write("Random sampling is an audit technique used to select a sample of items from a population to analyse. The items are selected randomly and independently of each other, giving each item an equal chance of being chosen. This technique is used to reduce the cost and time of auditing and to reduce the risk of bias in the sample. Random sampling can be used to audit any population, from financial transactions to customer feedback. It is a useful tool for auditors to gain an understanding of the population and make informed decisions about the results of the audit.")   
    st.write("Stratified sampling is a method of sampling that groups the population into mutually exclusive subgroups (or strata) and then randomly selects a sample from each stratum. In an audit environment, stratified sampling can be used to ensure that a representative sample from each subset of the population is selected and the audit process is based on reliable data. This method helps to reduce the risk of errors and inconsistencies in the audit process. Stratified sampling can also help to reduce the sample size required to achieve a desired level of accuracy. The method is particularly useful when the population is heterogeneous and the characteristics of the population are relevant to the audit process.")
def Random_Sampling():
    st.subheader("Random Sampling Generator")
    st.caption("Simple random sampling involves selecting a subset of the population without any predetermined pattern. Every member has an equal chance of being chosen.")
    st.markdown("Random Selection for Audit Sampling Guide") 
    col1, col2, col3 = st.columns((1,1.5,1.5))

    with col1:
           
        population = st.number_input("Population", min_value=1)
        sample = st.number_input("Sample", min_value=1, max_value=population)
       

        sample_percentage = (sample/population)*100
       
    with col2:
        st.write('The percentage of sample vs population is ', sample_percentage, '%')
        

        df = pd.DataFrame({
            'Parameters':['Population','Sample'],
            'Values':[population, sample],
            'Percentage%':[0,sample_percentage]
            })

        st.write(df)

    with col3:
        st.subheader('Generate Sample')
        st.caption("Click the slider to generate the samples randomly")
        sample_size = st.slider('Pick the desired sample size', 0,100)

        random_sample = np.random.randint(low=0, high=population, size=sample_size)
        st.write('The total sample size is:', sample_size)
        st.write('The random sample is:', random_sample)



def Stratified_Sampling():
    st.subheader('Stratified Sampling Calculator')
    st.caption("Stratified sampling is a sampling technique in which the population is divided into smaller subgroups, or strata, based on certain characteristics. A random sample is then taken from each stratum.")
    col1, col2, col3 = st.columns((1,1,2))
    with col1:
        # Get the number of strata
        n_strata = st.number_input('How many strata?', min_value=0, max_value=10, help="A strata is a classification group e.g., invoices, PO, receipts, etc.")

        # Get the populations of each strata
        populations = []
        sampling_percentages = []
        for i in range(n_strata):
            pop = st.number_input(f'What is the population of strata {i+1}?', min_value=0)
            samp_pct = st.number_input(f'What is the sampling percentage of strata {i+1}?', min_value=0, max_value=1000)
            populations.append(pop)
            sampling_percentages.append(samp_pct)

        # Calculate the total population
        total_population = sum(populations)

        # Calculate the total sample size
        total_sample_size = 0
        for pop, samp_pct in zip(populations, sampling_percentages):
            total_sample_size += (pop * samp_pct) / 100

        # Calculate the sampling percentage versus total population
        if total_population > 0:
            sampling_percentage_vs_total_population = (total_sample_size / total_population) * 100
        else:
            sampling_percentage_vs_total_population = 0

    with col2:
    # Display the results
        st.write(f'Total population: {total_population}')
        st.write(f'Total sample size: {total_sample_size}')
        st.write(f'Sampling percentage versus total population: {sampling_percentage_vs_total_population:.2f}%')
        # Create the sampling chart

        data = {'Strata': list(range(1, n_strata+1)),
                'Population': populations,
                'Sampling Percentage': sampling_percentages}
        
        st.caption("Please go back to random sampling to generate the random sample by each strata.")

    with col3:
        fig = px.bar(data, x='Strata', y=['Population', 'Sampling Percentage'], 
                     barmode='group',
                     height=600)
        st.plotly_chart(fig)


#Sidebar navigation
st.sidebar.markdown("Developed by Mark with ❤️")
love_icon = """ 
"""
st.sidebar.markdown("[Linkedin Profile](https://www.linkedin.com/in/mark-hofmann-ca-cpa-cia-crma-cfsa-20594822)")
st.sidebar.markdown(love_icon, unsafe_allow_html=True)

st.sidebar.subheader('Menu Navigator')
options = st.sidebar.radio('Choose the page the display:', ["Home", "Random Sampling", "Stratified Sampling"])

# Navigation options
if options == 'Home':
    Home()
elif options == 'Random Sampling':
    Random_Sampling()
elif options == 'Stratified Sampling':
    Stratified_Sampling()   
