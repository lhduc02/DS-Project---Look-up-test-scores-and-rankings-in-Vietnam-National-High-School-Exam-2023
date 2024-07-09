import pandas as pd
import matplotlib.pyplot as plt
import math
import streamlit as st
import base64
import plotly.express as px

# Background
df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("D:\\.Repo\\Project Repo\\DS Project --- Chatbot_THPTQG_2023\\image.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)



# Title
original_title = '<p style="font-family:Arial; color:Black; font-size: 32px; text-align: center; font-weight:600">CHATBOT TRA CỨU RANK CỦA THÍ SINH</p>'
st.markdown(original_title, unsafe_allow_html=True)


# Nhập thông tin
sbd_str = st.text_input("Nhập số báo danh của bạn")


# MAIN
# Khai báo
df = pd.read_csv("D:\\.Repo\\Project Repo\\DS Project --- Chatbot_THPTQG_2023\\diem_thi_thpt_2023.csv", dtype={'sbd': str})
df.columns = ['sbd','toan','van','nn','ly','hoa','sinh','su','dia','gdcd','ma_nn']
df['KHTN'] = df['ly'] + df['hoa'] + df['sinh']
df['KHXH'] = df['su'] + df['dia'] + df['gdcd']
df['N1'] = df[df['ma_nn'] == 'N1']['nn']
df['N1'] = df[df['ma_nn'] == 'N1']['nn']
df['N2'] = df[df['ma_nn'] == 'N2']['nn']
df['N3'] = df[df['ma_nn'] == 'N3']['nn']
df['N4'] = df[df['ma_nn'] == 'N4']['nn']
df['N5'] = df[df['ma_nn'] == 'N5']['nn']
df['N6'] = df[df['ma_nn'] == 'N6']['nn']
df['N7'] = df[df['ma_nn'] == 'N7']['nn']

df['sbd'] = df['sbd'].astype(str)
tinh = ['THÀNH PHỐ HÀ NỘI', 'THÀNH PHỐ HỒ CHÍ MINH', 'THÀNH PHỐ HẢI PHÒNG', 'THÀNH PHỐ ĐÀ NẴNG', 'TỈNH HÀ GIANG', 'TỈNH CAO BẰNG', 'TỈNH LAI CHÂU', 'TỈNH LÀO CAI', 'TỈNH TUYÊN QUANG', 'TỈNH LẠNG SƠN', 'TỈNH BẮC KẠN', 'TỈNH THÁI NGUYÊN', 'TỈNH YÊN BÁI', 'TỈNH SƠN LA', 
        'TỈNH PHÚ THỌ', 'TỈNH VĨNH PHÚC', 'TỈNH QUẢNG NINH', 'TỈNH BẮC GIANG', 'TỈNH BẮC NINH', 'TỈNH HẢI DƯƠNG', 'TỈNH HƯNG YÊN', 'TỈNH HÒA BÌNH', 'TỈNH HÀ NAM', 'TỈNH NAM ĐỊNH', 'TỈNH THÁI BÌNH', 'TỈNH NINH BÌNH', 'TỈNH THANH HÓA', 'TỈNH NGHỆ AN', 'TỈNH HÀ TĨNH', 
        'TỈNH QUẢNG BÌNH', 'TỈNH QUẢNG TRỊ', 'TỈNH THỪA THIÊN-HUẾ', 'TỈNH QUẢNG NAM', 'TỈNH QUẢNG NGÃI', 'TỈNH KON TUM', 'TỈNH BÌNH ĐỊNH', 'TỈNH GIA LAI', 'TỈNH PHÚ YÊN', 'TỈNH ĐĂK LĂK', 'TỈNH KHÁNH HÒA', 'TỈNH LÂM ĐỒNG', 'TỈNH BÌNH PHƯỚC', 'TỈNH BÌNH DƯƠNG', 
        'TỈNH NINH THUẬN', 'TỈNH TÂY NINH', 'TỈNH BÌNH THUẬN', 'TỈNH ĐỒNG NAI', 'TỈNH LONG AN', 'TỈNH ĐỒNG THÁP', 'TỈNH AN GIANG', 'TỈNH BÀ RỊA-VŨNG TÀU', 'TỈNH TIỀN GIANG', 'TỈNH KIÊN GIANG', 'THÀNH PHỐ CẦN THƠ', 'TỈNH BẾN TRE', 'TỈNH VĨNH LONG', 'TỈNH TRÀ VINH', 
        'TỈNH SÓC TRĂNG', 'TỈNH BẠC LIÊU', 'TỈNH CÀ MAU', 'TỈNH ĐIỆN BIÊN', 'TỈNH ĐĂK NÔNG', 'TỈNH HẬU GIANG']


sbd = df['sbd'].to_list()

for i in range(len(sbd)):
    if sbd_str == sbd[i]:
        index = i
        break



try:
    # Tránh in xấu
    if sbd_str != "":
        tmp = index
        st.write("Điểm thi thành phần của bạn là:")
        m1, m2, m3, m4, m5, m6, m7, m8, m9 = st.columns(9)
        with m1:
            st.write("Toán")
            st.write(df['toan'].iloc[index])
        with m2:
            st.write("Ngữ văn")
            st.write(df['van'].iloc[index])
        with m3:
            st.write("Ng.ngữ")
            st.write(df['nn'].iloc[index])
        with m4:
            st.write("Vật lý")
            st.write(df['ly'].iloc[index])
        with m5:
            st.write("Hóa học")
            st.write(df['hoa'].iloc[index])
        with m6:
            st.write("Sinh học")
            st.write(df['sinh'].iloc[index])
        with m7:
            st.write("Lịch sử")
            st.write(df['su'].iloc[index])
        with m8:
            st.write("Địa lý")
            st.write(df['dia'].iloc[index])
        with m9:
            st.write("GDCD")
            st.write(df['gdcd'].iloc[index])

        khoi = ""
        khoi = st.text_input("Nhập khối thi của bạn. Cần nhập đúng dạng (A00, A01,..., B00, B01,...)")

        # Tránh in xấu
        if khoi != "":
            # Check điểm các khối
            if khoi == 'A00':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['ly'].loc[index] + df['hoa'].loc[index]
                df['A00'] = df['toan'] + df['ly'] + df['hoa']
            elif khoi == 'A01':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['ly'].loc[index] + df['N1'].loc[index]
                df['A01'] = df['toan'] + df['ly'] + df['N1']
            elif khoi == 'A02':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['ly'].loc[index] + df['sinh'].loc[index]
                df['A02'] = df['toan'] + df['ly'] + df['sinh']
            elif khoi == 'A03':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['ly'].loc[index] + df['su'].loc[index]
                df['A03'] = df['toan'] + df['ly'] + df['su']
            elif khoi == 'A04':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['ly'].loc[index] + df['dia'].loc[index]
                df['A04'] = df['toan'] + df['ly'] + df['dia']
            elif khoi == 'A05':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['hoa'].loc[index] + df['su'].loc[index]
                df['A05'] = df['toan'] + df['hoa'] + df['su']
            elif khoi == 'A06':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['hoa'].loc[index] + df['dia'].loc[index]
                df['A06'] = df['toan'] + df['hoa'] + df['dia']
            elif khoi == 'A07':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['su'].loc[index] + df['dia'].loc[index]
                df['A07'] = df['toan'] + df['su'] + df['dia']
            elif khoi == 'A08':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['su'].loc[index] + df['gdcd'].loc[index]
                df['A08'] = df['toan'] + df['su'] + df['gdcd']
            elif khoi == 'A09':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['dia'].loc[index] + df['gdcd'].loc[index]
                df['A09'] = df['toan'] + df['dia'] + df['gdcd']
            elif khoi == 'A10':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['ly'].loc[index] + df['gdcd'].loc[index]
                df['A10'] = df['toan'] + df['ly'] + df['gdcd']
            elif khoi == 'A11':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['hoa'].loc[index] + df['gdcd'].loc[index]
                df['A11'] = df['toan'] + df['hoa'] + df['gdcd']
            elif khoi == 'A12':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['KHTN'].loc[index] + df['KHXH'].loc[index]
                df['A12'] = df['toan'] + df['KHTN'] + df['KHXH']
            elif khoi == 'A14':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['KHTN'].loc[index] + df['dia'].loc[index]
                df['A14'] = df['toan'] + df['KHTN'] + df['dia']
            elif khoi == 'A15':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['KHTN'].loc[index] + df['gdcd'].loc[index]
                df['A15'] = df['toan'] + df['KHTN'] + df['gdcd']
            elif khoi == 'A16':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['KHTN'].loc[index] + df['van'].loc[index]
                df['A16'] = df['toan'] + df['KHTN'] + df['van']
            elif khoi == 'A17':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['ly'].loc[index] + df['KHXH'].loc[index]
                df['A17'] = df['toan'] + df['ly'] + df['KHXH']
            elif khoi == 'A18':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['hoa'].loc[index] + df['KHXH'].loc[index]
                df['A18'] = df['toan'] + df['hoa'] + df['KHXH']
            elif khoi == 'B00':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['sinh'].loc[index] + df['hoa'].loc[index]
                df['B00'] = df['toan'] + df['sinh'] + df['hoa']
            elif khoi == 'B01':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['sinh'].loc[index] + df['su'].loc[index]
                df['B01'] = df['toan'] + df['sinh'] + df['su']
            elif khoi == 'B02':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['sinh'].loc[index] + df['dia'].loc[index]
                df['B02'] = df['toan'] + df['sinh'] + df['dia']
            elif khoi == 'B03':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['sinh'].loc[index] + df['van'].loc[index]
                df['B03'] = df['toan'] + df['sinh'] + df['van']
            elif khoi == 'B04':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['sinh'].loc[index] + df['gdcd'].loc[index]
                df['B04'] = df['toan'] + df['sinh'] + df['gdcd']
            elif khoi == 'B05':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['sinh'].loc[index] + df['KHXH'].loc[index]
                df['B05'] = df['toan'] + df['sinh'] + df['KHXH']
            elif khoi == 'B08':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['sinh'].loc[index] + df['N1'].loc[index]
                df['B08'] = df['toan'] + df['sinh'] + df['N1']
            elif khoi == 'C00':
                diem_cua_thi_sinh = df['van'].loc[index] + df['su'].loc[index] + df['dia'].loc[index]
                df['C00'] = df['van'] + df['su'] + df['dia']
            elif khoi == 'C01':
                diem_cua_thi_sinh = df['van'].loc[index] + df['toan'].loc[index] + df['ly'].loc[index]
                df['C01'] = df['van'] + df['toan'] + df['ly']
            elif khoi == 'C02':
                diem_cua_thi_sinh = df['van'].loc[index] + df['toan'].loc[index] + df['hoa'].loc[index]
                df['C02'] = df['van'] + df['toan'] + df['hoa']
            elif khoi == 'C03':
                diem_cua_thi_sinh = df['van'].loc[index] + df['toan'].loc[index] + df['su'].loc[index]
                df['C03'] = df['van'] + df['toan'] + df['su']
            elif khoi == 'C04':
                diem_cua_thi_sinh = df['van'].loc[index] + df['toan'].loc[index] + df['dia'].loc[index]
                df['C04'] = df['van'] + df['toan'] + df['dia']
            elif khoi == 'C05':
                diem_cua_thi_sinh = df['van'].loc[index] + df['ly'].loc[index] + df['hoa'].loc[index]
                df['C05'] = df['van'] + df['ly'] + df['hoa']
            elif khoi == 'C06':
                diem_cua_thi_sinh = df['van'].loc[index] + df['ly'].loc[index] + df['sinh'].loc[index]
                df['C06'] = df['van'] + df['ly'] + df['sinh']
            elif khoi == 'C07':
                diem_cua_thi_sinh = df['van'].loc[index] + df['ly'].loc[index] + df['su'].loc[index]
                df['C07'] = df['van'] + df['ly'] + df['su']
            elif khoi == 'C08':
                diem_cua_thi_sinh = df['van'].loc[index] + df['hoa'].loc[index] + df['sinh'].loc[index]
                df['C08'] = df['van'] + df['hoa'] + df['sinh']
            elif khoi == 'C09':
                diem_cua_thi_sinh = df['van'].loc[index] + df['ly'].loc[index] + df['dia'].loc[index]
                df['C09'] = df['van'] + df['ly'] + df['dia']
            elif khoi == 'C10':
                diem_cua_thi_sinh = df['van'].loc[index] + df['hoa'].loc[index] + df['su'].loc[index]
                df['C10'] = df['van'] + df['hoa'] + df['su']
            elif khoi == 'C12':
                diem_cua_thi_sinh = df['van'].loc[index] + df['sinh'].loc[index] + df['su'].loc[index]
                df['C12'] = df['van'] + df['sinh'] + df['su']
            elif khoi == 'C13':
                diem_cua_thi_sinh = df['van'].loc[index] + df['sinh'].loc[index] + df['dia'].loc[index]
                df['C13'] = df['van'] + df['sinh'] + df['dia']
            elif khoi == 'C14':
                diem_cua_thi_sinh = df['van'].loc[index] + df['toan'].loc[index] + df['gdcd'].loc[index]
                df['C14'] = df['van'] + df['toan'] + df['gdcd']
            elif khoi == 'C15':
                diem_cua_thi_sinh = df['van'].loc[index] + df['toan'].loc[index] + df['KHXH'].loc[index]
                df['C15'] = df['van'] + df['toan'] + df['KHXH']
            elif khoi == 'C16':
                diem_cua_thi_sinh = df['van'].loc[index] + df['ly'].loc[index] + df['gdcd'].loc[index]
                df['C16'] = df['van'] + df['ly'] + df['gdcd']
            elif khoi == 'C17':
                diem_cua_thi_sinh = df['van'].loc[index] + df['hoa'].loc[index] + df['gdcd'].loc[index]
                df['C17'] = df['van'] + df['hoa'] + df['gdcd']
            elif khoi == 'C19':
                diem_cua_thi_sinh = df['van'].loc[index] + df['su'].loc[index] + df['gdcd'].loc[index]
                df['C19'] = df['van'] + df['su'] + df['gdcd']
            elif khoi == 'C20':
                diem_cua_thi_sinh = df['van'].loc[index] + df['dia'].loc[index] + df['gdcd'].loc[index]
                df['C20'] = df['van'] + df['dia'] + df['gdcd']
            elif khoi == 'D01':
                diem_cua_thi_sinh = df['van'].loc[index] + df['toan'].loc[index] + df['N1'].loc[index]
                df['D01'] = df['van'] + df['toan'] + df['N1']
            elif khoi == 'D02':
                diem_cua_thi_sinh = df['van'].loc[index] + df['toan'].loc[index] + df['N2'].loc[index]
                df['D02'] = df['van'] + df['toan'] + df['N2']
            elif khoi == 'D03':
                diem_cua_thi_sinh = df['van'].loc[index] + df['toan'].loc[index] + df['N3'].loc[index]
                df['D03'] = df['van'] + df['toan'] + df['N3']
            elif khoi == 'D04':
                diem_cua_thi_sinh = df['van'].loc[index] + df['toan'].loc[index] + df['N4'].loc[index]
                df['D04'] = df['van'] + df['toan'] + df['N4']
            elif khoi == 'D05':
                diem_cua_thi_sinh = df['van'].loc[index] + df['toan'].loc[index] + df['N5'].loc[index]
                df['D05'] = df['van'] + df['toan'] + df['N5']
            elif khoi == 'D06':
                diem_cua_thi_sinh = df['van'].loc[index] + df['toan'].loc[index] + df['N6'].loc[index]
                df['D06'] = df['van'] + df['toan'] + df['N6']
            elif khoi == 'D07':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['hoa'].loc[index] + df['N1'].loc[index]
                df['D07'] = df['toan'] + df['hoa'] + df['N1']
            elif khoi == 'D08':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['sinh'].loc[index] + df['N1'].loc[index]
                df['D08'] = df['toan'] + df['sinh'] + df['N1']
            elif khoi == 'D09':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['su'].loc[index] + df['N1'].loc[index]
                df['D09'] = df['toan'] + df['su'] + df['N1']
            elif khoi == 'D10':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['dia'].loc[index] + df['N1'].loc[index]
                df['D10'] = df['toan'] + df['dia'] + df['N1']
            elif khoi == 'D11':
                diem_cua_thi_sinh = df['van'].loc[index] + df['ly'].loc[index] + df['N1'].loc[index]
                df['D11'] = df['van'] + df['ly'] + df['N1']
            elif khoi == 'D12':
                diem_cua_thi_sinh = df['van'].loc[index] + df['hoa'].loc[index] + df['N1'].loc[index]
                df['D12'] = df['van'] + df['hoa'] + df['N1']
            elif khoi == 'D13':
                diem_cua_thi_sinh = df['van'].loc[index] + df['sinh'].loc[index] + df['N1'].loc[index]
                df['D13'] = df['van'] + df['sinh'] + df['N1']
            elif khoi == 'D14':
                diem_cua_thi_sinh = df['van'].loc[index] + df['su'].loc[index] + df['N1'].loc[index]
                df['D14'] = df['van'] + df['su'] + df['N1']
            elif khoi == 'D15':
                diem_cua_thi_sinh = df['van'].loc[index] + df['dia'].loc[index] + df['N1'].loc[index]
                df['D15'] = df['van'] + df['dia'] + df['N1']
            elif khoi == 'D16':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['dia'].loc[index] + df['N5'].loc[index]
                df['D16'] = df['toan'] + df['dia'] + df['N5']
            elif khoi == 'D17':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['dia'].loc[index] + df['N2'].loc[index]
                df['D17'] = df['toan'] + df['dia'] + df['N2']
            elif khoi == 'D18':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['dia'].loc[index] + df['N6'].loc[index]
                df['D18'] = df['toan'] + df['dia'] + df['N6']
            elif khoi == 'D19':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['dia'].loc[index] + df['N3'].loc[index]
                df['D19'] = df['toan'] + df['dia'] + df['N3']
            elif khoi == 'D20':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['dia'].loc[index] + df['N4'].loc[index]
                df['D20'] = df['toan'] + df['dia'] + df['N4']
            elif khoi == 'D21':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['hoa'].loc[index] + df['N5'].loc[index]
                df['D21'] = df['toan'] + df['hoa'] + df['N5']
            elif khoi == 'D22':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['hoa'].loc[index] + df['N2'].loc[index]
                df['D22'] = df['toan'] + df['hoa'] + df['N2']
            elif khoi == 'D23':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['hoa'].loc[index] + df['N6'].loc[index]
                df['D23'] = df['toan'] + df['hoa'] + df['N6']
            elif khoi == 'D24':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['hoa'].loc[index] + df['N3'].loc[index]
                df['D24'] = df['toan'] + df['hoa'] + df['N3']
            elif khoi == 'D25':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['hoa'].loc[index] + df['N4'].loc[index]
                df['D25'] = df['toan'] + df['hoa'] + df['N4']
            elif khoi == 'D26':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['ly'].loc[index] + df['N5'].loc[index]
                df['D26'] = df['toan'] + df['ly'] + df['N5']
            elif khoi == 'D27':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['ly'].loc[index] + df['N2'].loc[index]
                df['D27'] = df['toan'] + df['ly'] + df['N2']
            elif khoi == 'D28':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['ly'].loc[index] + df['N6'].loc[index]
                df['D28'] = df['toan'] + df['ly'] + df['N6']
            elif khoi == 'D29':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['ly'].loc[index] + df['N3'].loc[index]
                df['D29'] = df['toan'] + df['ly'] + df['N3']
            elif khoi == 'D30':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['ly'].loc[index] + df['N4'].loc[index]
                df['D30'] = df['toan'] + df['ly'] + df['N4']
            elif khoi == 'D31':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['sinh'].loc[index] + df['N5'].loc[index]
                df['D31'] = df['toan'] + df['sinh'] + df['N5']
            elif khoi == 'D32':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['sinh'].loc[index] + df['N2'].loc[index]
                df['D32'] = df['toan'] + df['sinh'] + df['N2']
            elif khoi == 'D33':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['sinh'].loc[index] + df['N6'].loc[index]
                df['D33'] = df['toan'] + df['sinh'] + df['N6']
            elif khoi == 'D34':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['sinh'].loc[index] + df['N3'].loc[index]
                df['D34'] = df['toan'] + df['sinh'] + df['N3']
            elif khoi == 'D35':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['sinh'].loc[index] + df['N4'].loc[index]
                df['D35'] = df['toan'] + df['sinh'] + df['N4']
            elif khoi == 'D41':
                diem_cua_thi_sinh = df['van'].loc[index] + df['dia'].loc[index] + df['N5'].loc[index]
                df['D41'] = df['van'] + df['dia'] + df['N5']
            elif khoi == 'D42':
                diem_cua_thi_sinh = df['van'].loc[index] + df['dia'].loc[index] + df['N2'].loc[index]
                df['D42'] = df['van'] + df['dia'] + df['N2']
            elif khoi == 'D43':
                diem_cua_thi_sinh = df['van'].loc[index] + df['dia'].loc[index] + df['N6'].loc[index]
                df['D43'] = df['van'] + df['dia'] + df['N6']
            elif khoi == 'D44':
                diem_cua_thi_sinh = df['van'].loc[index] + df['dia'].loc[index] + df['N3'].loc[index]
                df['D44'] = df['van'] + df['dia'] + df['N3']
            elif khoi == 'D45':
                diem_cua_thi_sinh = df['van'].loc[index] + df['dia'].loc[index] + df['N4'].loc[index]
                df['D45'] = df['van'] + df['dia'] + df['N4']
            elif khoi == 'D52':
                diem_cua_thi_sinh = df['van'].loc[index] + df['ly'].loc[index] + df['N2'].loc[index]
                df['D52'] = df['van'] + df['ly'] + df['N2']
            elif khoi == 'D54':
                diem_cua_thi_sinh = df['van'].loc[index] + df['ly'].loc[index] + df['N3'].loc[index]
                df['D54'] = df['van'] + df['ly'] + df['N3']
            elif khoi == 'D55':
                diem_cua_thi_sinh = df['van'].loc[index] + df['ly'].loc[index] + df['N4'].loc[index]
                df['D55'] = df['van'] + df['ly'] + df['N4']
            elif khoi == 'D61':
                diem_cua_thi_sinh = df['van'].loc[index] + df['su'].loc[index] + df['N5'].loc[index]
                df['D61'] = df['van'] + df['su'] + df['N5']
            elif khoi == 'D62':
                diem_cua_thi_sinh = df['van'].loc[index] + df['su'].loc[index] + df['N2'].loc[index]
                df['D62'] = df['van'] + df['su'] + df['N2']
            elif khoi == 'D63':
                diem_cua_thi_sinh = df['van'].loc[index] + df['su'].loc[index] + df['N6'].loc[index]
                df['D63'] = df['van'] + df['su'] + df['N6']
            elif khoi == 'D64':
                diem_cua_thi_sinh = df['van'].loc[index] + df['su'].loc[index] + df['N3'].loc[index]
                df['D64'] = df['van'] + df['su'] + df['N3']
            elif khoi == 'D65':
                diem_cua_thi_sinh = df['van'].loc[index] + df['su'].loc[index] + df['N4'].loc[index]
                df['D65'] = df['van'] + df['su'] + df['N4']
            elif khoi == 'D66':
                diem_cua_thi_sinh = df['van'].loc[index] + df['gdcd'].loc[index] + df['N1'].loc[index]
                df['D66'] = df['van'] + df['gdcd'] + df['N1']
            elif khoi == 'D68':
                diem_cua_thi_sinh = df['van'].loc[index] + df['gdcd'].loc[index] + df['N2'].loc[index]
                df['D68'] = df['van'] + df['gdcd'] + df['N2']
            elif khoi == 'D69':
                diem_cua_thi_sinh = df['van'].loc[index] + df['gdcd'].loc[index] + df['N6'].loc[index]
                df['D69'] = df['van'] + df['gdcd'] + df['N6']
            elif khoi == 'D70':
                diem_cua_thi_sinh = df['van'].loc[index] + df['gdcd'].loc[index] + df['N3'].loc[index]
                df['D70'] = df['van'] + df['gdcd'] + df['N3']
            elif khoi == 'D72':
                diem_cua_thi_sinh = df['van'].loc[index] + df['KHTN'].loc[index] + df['N1'].loc[index]
                df['D72'] = df['van'] + df['KHTN'] + df['N1']
            elif khoi == 'D73':
                diem_cua_thi_sinh = df['van'].loc[index] + df['KHTN'].loc[index] + df['N5'].loc[index]
                df['D73'] = df['van'] + df['KHTN'] + df['N5']
            elif khoi == 'D74':
                diem_cua_thi_sinh = df['van'].loc[index] + df['KHTN'].loc[index] + df['N2'].loc[index]
                df['D74'] = df['van'] + df['KHTN'] + df['N2']
            elif khoi == 'D75':
                diem_cua_thi_sinh = df['van'].loc[index] + df['KHTN'].loc[index] + df['N6'].loc[index]
                df['D75'] = df['van'] + df['KHTN'] + df['N6']
            elif khoi == 'D76':
                diem_cua_thi_sinh = df['van'].loc[index] + df['KHTN'].loc[index] + df['N3'].loc[index]
                df['D76'] = df['van'] + df['KHTN'] + df['N3']
            elif khoi == 'D77':
                diem_cua_thi_sinh = df['van'].loc[index] + df['KHTN'].loc[index] + df['N4'].loc[index]
                df['D77'] = df['van'] + df['KHTN'] + df['N4']
            elif khoi == 'D78':
                diem_cua_thi_sinh = df['van'].loc[index] + df['KHXH'].loc[index] + df['N1'].loc[index]
                df['D78'] = df['van'] + df['KHXH'] + df['N1']
            elif khoi == 'D79':
                diem_cua_thi_sinh = df['van'].loc[index] + df['KHXH'].loc[index] + df['N5'].loc[index]
                df['D79'] = df['van'] + df['KHXH'] + df['N5']
            elif khoi == 'D80':
                diem_cua_thi_sinh = df['van'].loc[index] + df['KHXH'].loc[index] + df['N2'].loc[index]
                df['D80'] = df['van'] + df['KHXH'] + df['N2']
            elif khoi == 'D81':
                diem_cua_thi_sinh = df['van'].loc[index] + df['KHXH'].loc[index] + df['N6'].loc[index]
                df['D81'] = df['van'] + df['KHXH'] + df['N6']
            elif khoi == 'D82':
                diem_cua_thi_sinh = df['van'].loc[index] + df['KHXH'].loc[index] + df['N3'].loc[index]
                df['D82'] = df['van'] + df['KHXH'] + df['N3']
            elif khoi == 'D83':
                diem_cua_thi_sinh = df['van'].loc[index] + df['KHXH'].loc[index] + df['N4'].loc[index]
                df['D83'] = df['van'] + df['KHXH'] + df['N4']
            elif khoi == 'D84':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['gdcd'].loc[index] + df['N1'].loc[index]
                df['D84'] = df['toan'] + df['gdcd'] + df['N1']
            elif khoi == 'D85':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['gdcd'].loc[index] + df['N5'].loc[index]
                df['D85'] = df['toan'] + df['gdcd'] + df['N5']
            elif khoi == 'D86':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['gdcd'].loc[index] + df['N2'].loc[index]
                df['D86'] = df['toan'] + df['gdcd'] + df['N2']
            elif khoi == 'D87':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['gdcd'].loc[index] + df['N3'].loc[index]
                df['D87'] = df['toan'] + df['gdcd'] + df['N3']
            elif khoi == 'D88':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['gdcd'].loc[index] + df['N6'].loc[index]
                df['D88'] = df['toan'] + df['gdcd'] + df['N6']
            elif khoi == 'D90':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['KHTN'].loc[index] + df['N1'].loc[index]
                df['D90'] = df['toan'] + df['KHTN'] + df['N1']
            elif khoi == 'D91':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['KHTN'].loc[index] + df['N3'].loc[index]
                df['D91'] = df['toan'] + df['KHTN'] + df['N3']
            elif khoi == 'D92':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['KHTN'].loc[index] + df['N5'].loc[index]
                df['D92'] = df['toan'] + df['KHTN'] + df['N5']
            elif khoi == 'D93':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['KHTN'].loc[index] + df['N2'].loc[index]
                df['D93'] = df['toan'] + df['KHTN'] + df['N2']
            elif khoi == 'D94':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['KHTN'].loc[index] + df['N6'].loc[index]
                df['D94'] = df['toan'] + df['KHTN'] + df['N6']
            elif khoi == 'D95':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['KHTN'].loc[index] + df['N4'].loc[index]
                df['D95'] = df['toan'] + df['KHTN'] + df['N4']
            elif khoi == 'D96':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['KHXH'].loc[index] + df['N1'].loc[index]
                df['D96'] = df['toan'] + df['KHXH'] + df['N1']
            elif khoi == 'D97':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['KHXH'].loc[index] + df['N3'].loc[index]
                df['D97'] = df['toan'] + df['KHXH'] + df['N3']
            elif khoi == 'D98':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['KHXH'].loc[index] + df['N5'].loc[index]
                df['D98'] = df['toan'] + df['KHXH'] + df['N5']
            elif khoi == 'D99':
                diem_cua_thi_sinh = df['toan'].loc[index] + df['KHXH'].loc[index] + df['N2'].loc[index]
                df['D99'] = df['toan'] + df['KHXH'] + df['N2']
            else:
                st.write("Khối thi của bạn không được hỗ trợ tính toán hoặc bạn nhập sai khối thi. Bạn hãy chọn khối thi khác.")



            df = df[['sbd', khoi]]

            vi_tri_dau_tien = [0,102095,186946,209669,222802,229088,234134,237972,245838,80000,99999,266500,282653,290888,302661,318535,332577,348602,369682,386406,408340,423726,433416,443051,463456,484301,495450,531930,186946,586065,
                               597233,605646,618675,635872,649742,654770,673667,688528,209669,720236,734723,749410,760340,774558,780679,790908,803808,836966,222802,868297,888239,901164,916619,931042,943103,955220,965655,974851,229088,
                               991278,1001054,1007739,1015123,1022060] # vị trí (số báo danh) đầu tiên theo tỉnh thành

            # Xác định mã tỉnh
            if len(sbd_str) == 7:
                mt = int(sbd_str[0]) - 1  # mã tỉnh
            elif len(sbd_str) == 8:
                mt = int(sbd_str[:2]) - 2     # mã tỉnh
            else:
                st.write("Bạn nhập sai số báo danh!")



            # Xác định tỉnh của thí sinh
            if mt in [i for i in range(1, 20)]:
                tinh_cua_thi_sinh = tinh[mt]
            else:
                tinh_cua_thi_sinh = tinh[mt]



            if math.isnan(diem_cua_thi_sinh):
                st.write("Bạn không đủ điểm thành phần để tính điểm khối", khoi)

            else:
                diem_cua_thi_sinh = round(diem_cua_thi_sinh, 2)
                st.write("Điểm khối", khoi, "của bạn là: ", diem_cua_thi_sinh)
                
                # Tỉnh thành
                df_tinh = df.loc[vi_tri_dau_tien[mt]:vi_tri_dau_tien[mt+1]-1]
                df_tinh_cleaned = df_tinh.dropna()
                count_tinh = len(df_tinh_cleaned)
                sort_tinh = sorted(df_tinh_cleaned[khoi].to_list(), reverse = True)
                st.write("Xếp hạng điểm khối", khoi, "của bạn tại", tinh_cua_thi_sinh, "là:", sort_tinh.index(diem_cua_thi_sinh), "trên tổng số", count_tinh, "thí sinh")
                # Toàn quốc
                df_toan_quoc_cleaned = df.dropna()
                count_toan_quoc = len(df_toan_quoc_cleaned)
                sort_toan_quoc = sorted(df_toan_quoc_cleaned[khoi].to_list(), reverse = True)
                
                st.write("Xếp hạng điểm khối", khoi, "của bạn trên toàn quốc là:", sort_toan_quoc.index(diem_cua_thi_sinh), "trên tổng số", count_toan_quoc, "thí sinh")

except:
    st.write("Bạn nhập sai số báo danh hoặc số báo danh không tồn tại trong dữ liệu của Bộ GD&ĐT. Mời bạn nhập lại.")

