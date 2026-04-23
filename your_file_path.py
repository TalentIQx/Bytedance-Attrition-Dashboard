st.set_page_config(
    page_title="Bytedance Vibrant Dashboard",
    page_icon="🌟",
    layout="wide"
)


# ── CSV Upload Block (auto-added by Deploy Agent) ───────────────────────────
uploaded_file = st.file_uploader(
    "📂 Upload your CSV file",
    type=["csv"],
    help="Export from your HRIS system and upload here.",
)
if uploaded_file is None:
    st.info("👆 Please upload a CSV file to get started.")
    st.stop()
try:
    df = pd.read_csv(uploaded_file)
    st.success(f"✅ File loaded — {len(df):,} rows × {len(df.columns)} columns")
    with st.expander("👀 Preview first 10 rows"):
        st.dataframe(df.head(10), use_container_width=True)
except Exception as e:
    st.error(f"❌ Could not read CSV: {e}")
    st.stop()
# ── End CSV Upload Block ────────────────────────────────────────────────────