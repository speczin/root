import streamlit as st
st.sidebar.title('MENU')
#variaveis abaixo
paginaselecionada = st.sidebar.selectbox('Escolha uma opção abaixo:',['XP Calculator','Boss Pico'])
if paginaselecionada == 'XP Calculator':
   st.title('XP Calculator')
   level = st.slider('selecione seu level', 85,100)
   xp = st.slider('Quantos milhoes voce faz por ticket?',1,100)
   porc = st.slider('qual a sua % atual?',0,100)
   xp2 = (xp*1000000)
   po = porc/100
   if level == int('85'):
    st.info ('No level 85 voce precisa de {:.2f} bilhetes para evoluir'.format((682327150 -(po*682327150))/xp2))
   if level == int('86'):
        st.info('No level 86 voce precisa de {:.2f} bilhetes para evoluir'.format((695973690 - (po * 695973690)) / xp2))
   if level == int('87'):
        st.info('No level 87 voce precisa de {:.2f} bilhetes para evoluir'.format((709893160 - (po * 709893160)) / xp2))
   if level == int('88'):
        st.info('No level 88 voce precisa de {:.2f} bilhetes para evoluir'.format((724091020 - (po * 724091020)) / xp2))
   if level == int('89'):
    st.info('No level 89 voce precisa de {:.2f} bilhetes para evoluir'.format((738572840 - (po * 738572840)) / xp2))
   if level == int('90'):
        st.info('No level 90 voce precisa de {:.2f} bilhetes para evoluir'.format((753344300 - (po * 753344300)) / xp2))
   if level == int('91'):
        st.info('No level 91 voce precisa de {:.2f} bilhetes para evoluir'.format((1521755490 - (po * 1521755490)) / xp2))
   if level == int('92'):
        st.info('No level 92 voce precisa de {:.2f} bilhetes para evoluir'.format((1552190600 - (po * 1552190600)) / xp2))
   if level == int('93'):
    st.info('No level 93 voce precisa de {:.2f} bilhetes para evoluir'.format((1583234410 - (po * 1583234410)) / xp2))
   if level == int('94'):
        st.info('No level 94 voce precisa de {:.2f} bilhetes para evoluir'.format((1614899100 - (po * 1614899100)) / xp2))
   if level == int('95'):
    st.info('No level 95 voce precisa de {:.2f} bilhetes para evoluir'.format((1647197080 - (po * 1647197080)) / xp2))
   if level == int('96'):
    st.info('No level 96 voce precisa de {:.2f} bilhetes para evoluir'.format((1680141020 - (po * 1680141020)) / xp2))
   if level == int('97'):
        st.info('No level 97 voce precisa de {:.2f} bilhetes para evoluir'.format((1713743840 - (po * 1713743840)) / xp2))
   if level == int('98'):
    st.info('No level 98 voce precisa de {:.2f} bilhetes para evoluir'.format((1748018720 - (po * 1748018720)) / xp2))
   if level == int('99'):
    st.info('No level 99 voce precisa de {:.2f} bilhetes para evoluir'.format((1782979090 - (po * 1782979090)) / xp2))
   if level == int('100'):
    st.info('No level {1} voce precisa de {0:.2f} bilhetes para evoluir'.format((1818638670 - (po * 1818638670)) / xp2,level))
   st.write('\n---Dev by speczinn---')
if paginaselecionada == 'Boss Pico':
    st.title('Em construção')
