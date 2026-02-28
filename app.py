import streamlit as st
from openai import OpenAI
import os

# إعداد واجهة المستخدم بروح "البرمجيات الخضراء"
st.set_page_config(page_title="Ashraf AI Platform 2026", page_icon="🌿")

st.title("🚀 منصة أشرف للذكاء الاصطناعي المستدام")
st.markdown("---")

# إعداد العميل (Client) - يفضل وضع المفتاح في Secrets
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# منطقة الدردشة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال مدخلات المستخدم
if prompt := st.chat_input("كيف يمكنني مساعدتك في مشروعك الأخضر اليوم؟"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # رد الذكاء الاصطناعي
    with st.chat_message("assistant"):
        # ملاحظة: هنا يتم الربط الفعلي مع النموذج
        response = "هذا الرد تجريبي.. بمجرد وضع API Key سأقوم بتحليل: " + prompt
        st.markdown(response)
        
    st.session_state.messages.append({"role": "assistant", "content": response})
