import streamlit as st

st.title("Caulculadora de IMC")
#área de inputs
try:
    name = st.text_input("Digite seu nome: ")
    altura = st.number_input("Digite sua altura: ")
    peso = st.number_input("Digite seu peso: ")

    imc = peso/(altura**2)


#área das condições
    if st.button("Calcular"):
        if imc < 18.5:
            st.write(f"{name} Seu IMC {imc:.2f} Abaixo do peso 🟦")

        elif imc <24.9:
            st.write(f'{name} Seu IMC {imc:.2f} Peso normal 🟩')
            
        elif imc < 29.9:
            st.write(f"{name} Seu IMC {imc:.2f} Sobre peso 🟨")
            
        elif imc < 34.9:
            st.write(f"{name} Seu IMC {imc:.2f} Obesidade grau I 🟧")
            
        elif imc < 39.9:
            st.write(f"{name} Seu IMC {imc:.2f} Obesidade grau II 🟥")
            
        else:
            st.write(f"{name} Seu IMC {imc:.2f} Obesidade grau III ⬛ ")

        with open ("Site.txt","a") as arquivo:
            arquivo.write(f'|{imc:.2f} | {name}\n')
            
except ValueError:
    st.write("Valor invalido 😢, Tente um valor sem: ', ; @ ! 3 $ % ¨ & * ()'")