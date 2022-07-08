import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import requests
from streamlit_lottie import st_lottie
import base64





# Creating the sidebar menu

st.set_page_config(page_title='Dataware Demo Platform', layout='wide')

#st.sidebar.image('images/logo.png', width=300)

st.sidebar.markdown('##')
st.image('images/logo.png')
st.sidebar.markdown('##')

selected = option_menu(None, ["Platform", "Solutions", "Dataware", 'Settings'],
	icons=['house', 'cloud-upload', "list-task", 'gear'], menu_icon="cast",
	default_index=0, orientation="horizontal")


#with open('style.css') as f:
	#st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.3/font/bootstrap-icons.css">',
	unsafe_allow_html=True)
	



#-----------------------------------------------------------------------------------------------------------------------
# THIS IS THE PLATFORM SECTION
#------------------------------------------------------------------------------------------------------------------------

if selected == "Platform":
	st.header("Platform")




#------------------------------------------------------------------------------------------------------------------------
# THIS IS THE SOLUTIONS SECTION
#------------------------------------------------------------------------------------------------------------------------



if selected == "Solutions":
	st.markdown("<h2 style='font-weight:bold;text-align:center;text-decoration:underline;text-underline-offset:0.7em;\
                text-decoration-color:#e8573f;'>SOLUTIONS</h2>", unsafe_allow_html=True)  

	st.markdown("##")
	st.markdown("##")

	col1, col2= st.columns(2)

	with col1:
		st.markdown("<h4 style='font-weight:bold;font-size:30px'>ABOUT DATAWARE</h4><p style='text-align:justify;font-size:20px; \
                    font-family:'Lato' Sans-serif;'> \
                    Dataware is an award-winning African tech firm that provides big data, analytics, and cloud \
                    computing services. We strive to provide cutting edge data solutions to solve problems.",unsafe_allow_html=True)

		st.markdown("##")
		st.markdown("##")
		

		st.markdown("</p><p style='font-weight:bold;font-size:30px;'>WHAT PROBLEM ARE WE SOLVING?</p>  \
                    <p style='text-align:justify;font-size:20px;font-family:'Lato' Sans-serif;'>In today’s global market, \
                    limited customer and operational insights prevents the innovative assessment of customers and risks \
                    which impacts business growth and sustainability. Our contribution to this effort is to provide an \
                    end to end customizable and scalable range of solutions to enable you to get deeper insights on \
                    customer behaviour and business operations to inform decision making in real time.</p>",
                    unsafe_allow_html=True)


	with col2:
		def load_lottieurl(url:str):
			r = requests.get(url)
			if r.status_code != 200:
				return None
			return r.json()

		rep_anime = "https://assets8.lottiefiles.com/packages/lf20_npjqm3yq.json"
		rep_anime_json = load_lottieurl(rep_anime)
		st_lottie(rep_anime_json)


	st.markdown("##")
	st.markdown("##")
	st.markdown("##")
	st.markdown("##")

	#------------------------------------------------------------------------------------------------------------------------
	# THIS IS THE INDUSTRY EXPERTISE SECTION
	#------------------------------------------------------------------------------------------------------------------------


	st.markdown("<h2 style='text-align:center;text-decoration:underline;text-underline-offset:0.7em;\
                text-decoration-color:#e8573f;'>Industry Expertise</h2>", unsafe_allow_html=True)

	st.markdown("##")
	st.markdown("##")
	st.markdown("##")


	col3, col4, col5 = st.columns(3)

	#FINANCE-------------------------------------------------------------------------------------------------

	with col3:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:30em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'> \
			<center><i style='font-size:25px' class='bi bi-building'></i>\
			<p style='font-size:25px'>Finance</p>\
			<p>Spmething Spmething Spmething Spmething Spmething Spmething Spmething </p>\
			<p>Spmething Spmething Spmething Spmething Spmething Spmething Spmething </p>\
			<br><br><br>\
			<button class='t1'style='background-color:#F35106;color:white; border:None;border-radius:10px;\
			padding:15px;min-height:30px;min-width: 120px;' type='button'>\
			DEMO<i class='bi bi-chevron-double-right'></i></button>\
			</center></div>",
			unsafe_allow_html=True)
	#AGRICULTURE-------------------------------------------------------------------------------------------------

	with col4:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:30em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'> \
			<center><i style='font-size:25px' class='bi bi-snow3'></i><p style='font-size:25px'>Agriculture</p>\
			<p>Spmething Spmething Spmething Spmething Spmething Spmething Spmething </p>\
			<p>Spmething Spmething Spmething Spmething Spmething Spmething Spmething </p>\
			<br><br><br>\
			<button class='t1'style='background-color:#F35106;color:white; border:None;border-radius:10px;\
			padding:15px;min-height:30px;min-width: 120px;' type='button'>\
			DEMO<i class='bi bi-chevron-double-right'></i></button>\
			</center></div>",
			unsafe_allow_html=True)
	#HEALTH-------------------------------------------------------------------------------------------------
	with col5:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:30em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'> \
			<center><i  style='font-size:25px' class='bi bi-heart-pulse'></i>\
			<p style='font-size:25px'>Healthcare</p>\
			<p>Spmething Spmething Spmething Spmething Spmething Spmething Spmething </p>\
			<p>Spmething Spmething Spmething Spmething Spmething Spmething Spmething </p>\
			<br><br><br>\
			<button class='t1'style='background-color:#F35106;color:white; border:None;border-radius:10px;\
			padding:15px;min-height:30px;min-width: 120px;' type='button'>\
			DEMO<i class='bi bi-chevron-double-right'></i></button>\
			</center></div>",
			unsafe_allow_html=True)
	st.markdown("##")
	st.markdown("##")

	col6, col7, col8 = st.columns(3)

	#MARKETING-------------------------------------------------------------------------------------------------
	with col6:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:30em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'> \
			<center><i style='font-size:25px' class='bi bi-bag-heart'></i>\
			<p style='font-size:25px'>Marketing, Retail & eCommerce</p>\
			<p>Spmething Spmething Spmething Spmething Spmething Spmething Spmething </p>\
			<p>Spmething Spmething Spmething Spmething Spmething Spmething Spmething </p>\
			<br><br><br>\
			<button class='t1'style='background-color:#F35106;color:white; border:None;border-radius:10px;\
			padding:15px;min-height:30px;min-width: 120px;' type='button'>\
			DEMO<i class='bi bi-chevron-double-right'></i></button>\
			</center></div>",
			unsafe_allow_html=True)

	#EDUCATION-------------------------------------------------------------------------------------------------
	with col7:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:30em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'> \
			<center><i style='font-size:25px' class='bi bi-mortarboard'></i>\
			<p style='font-size:25px'>Education</p>\
			<p>Spmething Spmething Spmething Spmething Spmething Spmething Spmething </p>\
			<p>Spmething Spmething Spmething Spmething Spmething Spmething Spmething </p>\
			<br><br><br>\
			<button class='t1'style='background-color:#F35106;color:white; border:None;border-radius:10px;\
			padding:15px;min-height:30px;min-width: 120px;' type='button'>\
			DEMO<i class='bi bi-chevron-double-right'></i></button>\
			</center></div>",
			unsafe_allow_html=True)

	#IMPORT&EXPORT-------------------------------------------------------------------------------------------------
	with col8:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:30em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'> \
			<center><i style='font-size:25px' class='bi bi-box-seam'>\
			</i><i style='font-size:20px' class='bi bi-arrow-left-right'></i>\
			<p style='font-size:25px'>Import & Export</p>\
			<p>Spmething Spmething Spmething Spmething Spmething Spmething Spmething </p>\
			<p>Spmething Spmething Spmething Spmething Spmething Spmething Spmething </p>\
			<br><br><br>\
			<button class='t1'style='background-color:#F35106;color:white; border:None;border-radius:10px;\
			padding:15px;min-height:30px;min-width: 120px;' type='button'>\
			DEMO<i class='bi bi-chevron-double-right'></i></button>\
			</center></div>",
			unsafe_allow_html=True)

	st.markdown("##")
	st.markdown("##")
	st.markdown("##")
	st.markdown("##")
	st.markdown("##")
	st.markdown("##")

	col8,col9,col10 = st.columns([1,11,1])
	with col8:
		st.markdown(" ")
	with col9:
		st.image("images/lucent.png")
	with col10:
		st.markdown(" ")


	st.markdown("##")
	st.markdown("##")
	st.markdown("##")
	st.markdown("##")
	st.markdown("##")
	st.markdown("##")

	st.markdown("<h2 style='text-align:center;text-decoration:underline;text-underline-offset:0.7em;\
                text-decoration-color:#e8573f;'>High Impact Use Cases</h2>", unsafe_allow_html=True)

	st.markdown("##")
	st.markdown("##")
	st.markdown("##")

	col11,col12,col13,col14 = st.columns(4)
	with col11:
		sent_img = "sentiment.png"
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:10em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'>\
			<center><img src='image/sentiment.png;base64,{base64.b64encode(open(sent_img, 'rb').read()).decode()}'>\
			<p style='font-weight:bold'>Customer Churn Prediction</p></center></div>",
			unsafe_allow_html=True)
	with col12:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:10em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'>\
			<center><p style='font-weight:bold'>Customer Lifetime Value</p></center></div>",
			unsafe_allow_html=True)
	with col13:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:10em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'>\
			<center><p style='font-weight:bold'>Customer Segmentation</p></center></div>",
			unsafe_allow_html=True)
	with col14:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:10em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'>\
			<center><p style='font-weight:bold'>Risk Assessment<p></center></div>",
			unsafe_allow_html=True)

	st.markdown("##")

	col15,col16,col17,col18 = st.columns(4)
	with col15:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:10em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'>\
			<center><p style='font-weight:bold'>Sentiment Analysis</p></center></div>",
			unsafe_allow_html=True)
	with col16:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:10em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'>\
			<center><p style='font-weight:bold'>Crop Yield Prediction</p></center></div>",
			unsafe_allow_html=True)
	with col17:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:10em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'>\
			<center><p style='font-weight:bold'>Crop Disease Detection</p></center></div>",
			unsafe_allow_html=True)
	with col18:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:10em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'>\
			<center><p style='font-weight:bold'>Market Basket Analysis<p></center></div>",
			unsafe_allow_html=True)





	#-----------------------------------------------------------------------------------------------------------------------
	# THIS IS THE PLOTFORM SECTION
	#------------------------------------------------------------------------------------------------------------------------	

#-----------------------------------------------------------------------------------------------------------------------
# THIS IS THE PLOTFORM SECTION
#------------------------------------------------------------------------------------------------------------------------
if selected == "Dataware":
	st.header("Dataware")
