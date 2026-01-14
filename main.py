import streamlit as st
from core.config import CATEGORIES, THEME_COLORS

# Page Configuration
st.set_page_config(
    page_title="Antigravity News",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load Custom CSS
def load_css():
    with open("assets/style.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

try:
    load_css()
except FileNotFoundError:
    pass

# Header
st.title("Antigravity News 🌌")
st.markdown("### Defy the Noise. Elevate your Intel.")

# Navigation
tabs = st.tabs(CATEGORIES)

# Placeholder Content for Tabs
for i, tab in enumerate(tabs):
    with tab:
        category = CATEGORIES[i]
        st.header(f"{category} News")
        
        if st.button(f"{category} を更新", key=f"btn_{i}"):
            with st.spinner("最新ニュースを取得中..."):
                # For now, fetching ALL feeds for every tab (filtering to be added)
                # Ideally pass category to fetcher
                from core.fetcher import fetch_all
                from core.sorter import sort_articles
                from core.translator import translate_text
                
                raw_articles = fetch_all()
                sorted_articles = sort_articles(raw_articles)
                
                if sorted_articles:
                    # Display top 30
                    for article in sorted_articles[:30]:
                        with st.container():
                            col1, col2 = st.columns([3, 1])
                            with col1:
                                # Translate title
                                title = article['title']
                                try:
                                    title_ja = translate_text(title)
                                except:
                                    title_ja = title
                                
                                st.subheader(title_ja)
                                if title_ja != title:
                                    st.caption(f"原文: {title}")
                                
                                # Translate summary
                                summary = article.get('summary', '')
                                if summary:
                                    try:
                                        summary_ja = translate_text(summary[:300])
                                        st.write(summary_ja)
                                    except:
                                        st.write(summary)
                            
                            with col2:
                                st.caption(f"**{article.get('source', 'Unknown')}**")
                                st.caption(article.get('published', ''))
                                st.markdown(f"[記事を読む]({article['link']})")
                            
                            st.divider()
                else:
                    st.warning("記事が見つかりませんでした。")
