import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import requests
from streamlit_lottie import st_lottie
import base64
import pandas as pd








st.set_page_config(page_title='Dataware Demo Platform', layout='wide')

#------------------Background-Image-----------------------------------------

def set_bg_hack(main_bg):
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Adding CSS-----------------------------------------------------------------------------------------------------------

# Hiding Main Menu button
outter_css = """
<style>
#MainMenu{
	visibility: hidden;
}
</style>

"""
st.markdown(outter_css, unsafe_allow_html=True)


# Stylesheet link for bootstap icons
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.3/font/bootstrap-icons.css">',
	unsafe_allow_html=True)

#-------------------------------------------------------------------------------------------------------------------------




# Creating the sidebar menu
with st.sidebar:
	# Logo
	st.image('images/logo.png')
	st.markdown('##')
	selected = option_menu(None, ["About Us", "Platform", "Contact Us"],
		icons=['house', 'cpu', "person-rolodex"], menu_icon="cast",default_index=0)




	



#-----------------------------------------------------------------------------------------------------------------------
# THIS IS THE PLATFORM SECTION
#------------------------------------------------------------------------------------------------------------------------

if selected == "About Us":
	col1, col2= st.columns(2)

	with col1:
		st.markdown("<h4 style='font-weight:bold;font-size:30px;font-family:helvetica;color:#F35106'>Who we are</h4><p style='text-align:justify;font-size:20px; \
                    font-family:helvetica'> \
                    Dataware is an award-winning African tech firm that provides big data, analytics, and cloud \
                    computing services. We strive to provide cutting edge data solutions to solve problems.</p>",unsafe_allow_html=True)

		st.markdown("##")
		st.markdown("##")
		

		st.markdown("<p style='font-weight:bold;font-size:30px;font-family:helvetica;color:#F35106'>What problem are we solving?</p>  \
                    <p style='text-align:justify;font-size:20px;font-family:helvetica'>In today’s global market, \
                    limited customer and operational insights prevents the innovative assessment of customers and risks \
                    which impacts business growth and sustainability. Our contribution to this effort is to provide an \
                    end to end customizable and scalable range of solutions to enable you to get deeper insights on \
                    customer behaviour and business operations to inform decision making in real time.</p>",
                    unsafe_allow_html=True)


	with col2:
		st.image('images/img1.png')

	st.markdown("##")
	st.markdown("##")

	col3, col4 = st.columns([1,1.5])
	with col4:
		st.markdown("<p style='font-weight:bold;font-size:30px;font-family:helvetica;color:#F35106'>\
			What we stand for</p>",unsafe_allow_html=True)
		st.markdown("##")
		st.markdown("##")
		st.image('images/quote.png')

	with col3:
		st.image('images/vision.png')
		st.markdown("<p style='text-align:justify;font-size:20px;font-family:helvetica'>\
			Our values are Respect, Innovation, Passion, Continuous Learning and Service.</p>",unsafe_allow_html=True)


	st.markdown("##")
	st.markdown("##")
	st.markdown("##")
	st.markdown("##")




#------------------------------------------------------------------------------------------------------------------------
# THIS IS THE SOLUTIONS SECTION
#------------------------------------------------------------------------------------------------------------------------



if selected == "Platform":
	st.markdown("<h2 style='font-weight:bold;text-align:center;text-decoration:underline;text-underline-offset:0.7em;\
                text-decoration-color:#e8573f;'>SOLUTIONS</h2>", unsafe_allow_html=True)  

	st.markdown("##")
	st.markdown("##")

	col1, col2= st.columns(2)

	with col1:
		st.markdown("<p style='text-align:justify;font-size:20px;font-family:helvetica;'> \
                    Machine Learning is one of the branches of Artificial Intelligence (AI) that has \
                    the most future potential and offers the most benefits to the industry. \
                    According to the latest report by Grand View Research , the machine learning market will \
                    reach 96.7 billion dollars in 2025. A figure that is a dramatic increase considering that \
                    the figure in 2018 was 6.8 billion dollars. Over the next few years, more and more \
                    companies will opt for machine learning technology to improve their businesses.</p>",
                    unsafe_allow_html=True)

		st.markdown("##")
		st.markdown("##")
		

		st.markdown("<p style='text-align:justify;font-size:20px;font-family:helvetica;'>As a company, Dataware\
                    aims to assist businesses from a variety of sectors of industry to gain insights from data\
                    using Machine Learning, Big data as well as Cloud technologies.<br>\
                    This app seeks to provide a snapshot of the kind of use cases and solutions Machine Learning can\
                    provide in businesses in the technological space. It also serve the purpose of illustrating an\
                    aspect of the Dataware's interest, experiece and involvement in digitalization, technological advancement and automation\
                    for businesses in Africa.</p>",
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
			<div style='height:10em'>\
			<ul style='margin:0px;padding-right:0px'>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Customer Retention</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Asset Valuation</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Fraud Detection</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Churn Prediction</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Stock Prediction</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Loan Defaulting</li>\
			</ul>\
			</div>\
			<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>\
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
			<div style='height:10em'>\
			<ul style='margin:0px;padding-right:0px'>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Crop Yield Prediction</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Credit Scoring</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Fertilizer Recommendation</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Soil Nutrients</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Crop Disease Detection</li>\
			</ul>\
			</div>\
			<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>\
			<a href='https://vanessaattafynn-agric-demo-4aic4f.streamlitapp.com/'>\
			<button class='t1'style='background-color:#F35106;color:white; border:None;border-radius:10px;\
			padding:15px;min-height:30px;min-width: 120px;' type='button'>\
			DEMO<i class='bi bi-chevron-double-right'></i></button></a>\
			</center></div>",
			unsafe_allow_html=True)
	#HEALTH-------------------------------------------------------------------------------------------------
	with col5:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:30em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'> \
			<center><i  style='font-size:25px' class='bi bi-heart-pulse'></i>\
			<p style='font-size:25px'>Healthcare</p>\
			<div style='height:10em'>\
			<ul style='margin:0px;padding-right:0px'>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Disease Classification</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Medical Imagery</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Clustering</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Pattern Recognition</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Recommendations</li>\
			</ul>\
			</div>\
			<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>\
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
			<p style='font-size:25px'>Marketing & Retail</p>\
			<div style='height:10em'>\
			<ul style='margin:0px;padding-right:0px'>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Customer Segmenatation</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Sentiment Analysis</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Import & Export</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Churn Prediction</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Customer LTV</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Market Basket Analysis</li>\
			</ul>\
			</div>\
			<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>\
			<a href='https://vanessaattafynn-marketing-n-retail-ecom-vkejnj.streamlitapp.com/'>\
			<button class='t1'style='background-color:#F35106;color:white; border:None;border-radius:10px;\
			padding:15px;min-height:30px;min-width: 120px;' type='button'>\
			DEMO<i class='bi bi-chevron-double-right'></i></button></a>\
			</center></div>",
			unsafe_allow_html=True)

	#EDUCATION-------------------------------------------------------------------------------------------------
	with col7:
		st.markdown("<div style='border-radius:15px;padding:3em; \
			height:30em;box-shadow: 4px 3px 8px 1px #969696;-webkit-box-shadow: 4px 3px 8px 1px #969696;'> \
			<center><i style='font-size:25px' class='bi bi-mortarboard'></i>\
			<p style='font-size:25px'>Education</p>\
			<div style='height:10em'>\
			<ul style='margin:0px;padding-right:0px'>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Translations</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Formula Recognition</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Text to Speech</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Image to Text</li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'>Performace Prediction</li>\
			</ul>\
			</div>\
			<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>\
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
			<p style='font-size:25px'>Other Projects</p>\
			<div style='height:10em'>\
			<ul style='margin:0px;padding-right:0px'>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'></li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'></li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'></li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'></li>\
				<li style='background-color:#FDF7E4;color:#F35106;display:inline-block;border-radius:10px;padding-right:10px;font-size:14px;float:left'></li>\
			</ul>\
			</div>\
			<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>\
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
			<center><p style='font-weight:bold'>Customer Churn Prediction</p></center></div>",
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
			<center><p style='font-weight:bold'>Risk Assessment</p></center></div>",
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

#--------------------------------------------------------------------------------------------------------------------------
# THIS IS THE CONTACT US PAGE
#--------------------------------------------------------------------------------------------------------------------------
if selected == 'Contact Us':

    col1, col2 = st.columns([2,1])
    with col1:
    	def load_lottieurl(url:str):
    		r = requests.get(url)
    		if r.status_code != 200:
    			return None
    		return r.json()
    	contact_gif = "https://assets9.lottiefiles.com/packages/lf20_o31nf2ie.json"
    	contact_gif_json = load_lottieurl(contact_gif)
    	st_lottie(contact_gif_json)
    with col2:
    	st.markdown("##")
    	st.markdown("##")
    	st.markdown("##")
    	st.markdown("##")
    	st.markdown("##")
    	st.markdown("##")
    	st.markdown("<div align='left' style='font-family:helvetica'><p style='color:#F35106;font-size:2.5em;font-weight:bold'>Contact Information</p>\
    		<p style='font-size:20px;font-weight:bold'>Movenpick Ambassador Hotel<br>Emporium, 9th Floor<br>Independence Avenue<br>Accra</p>\
    		<p style='font-size:20px;font-weight:bold'>Call us: +233 (0) 30 263 3269</p>\
    		<p style='font-size:20px;font-weight:bold'>We are open from Monday - Friday<br>09:00am – 04:30pm GMT</p>\
    		<br><br><button class='t1'style='background-color:#F35106;color:white; border:None;border-radius:50px;\
			padding:15px;min-height:30px;min-width: 120px;font-size:20px;' type='button'>Schedule a Demo</button></div>", unsafe_allow_html=True)
