import streamlit as st
from PIL import Image, ImageDraw
from io import BytesIO

st.set_page_config(layout="wide")

st.title("🛰️ AI Change Detection via Aerial Imagery")
st.markdown("This demo simulates identifying unpermitted building changes using aerial photography and automated object detection.")

# Load before/after images
before = Image.open("ai_change_detection/images/before.png")
after = Image.open("ai_change_detection/images/after.png")

# Draw red box on the after image to simulate detection
after_with_box = after.copy()
draw = ImageDraw.Draw(after_with_box)
draw.rectangle([(1000, 640), (1250, 810)], outline="red", width=5)
draw.text((1000, 620), "New Structure Detected", fill="red")



# Side-by-side image layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📷 Before")
    st.image(before, use_container_width=True)

with col2:
    st.subheader("📷 After (with detection)")
    st.image(after_with_box, use_container_width=True)

# Explanatory Markdown box
st.markdown("""
> **Parcel Inspection Summary**
> 
> This visual demo highlights how change detection can be used to identify new construction in rural or agricultural parcels.
>
> - 📍 **Parcel ID**: 123456789  
> - 🕵️ **Detection Method**: Object recognition over aerial imagery  
> - 🏗️ **Detected Change**: New outbuilding  
> - 📅 **Detection Date**: May 2, 2025  
> 
> A field inspection is recommended to verify the update and revise property valuation accordingly.
""")

# Downloadable inspection report
report_text = """
Parcel ID: 123456789
Status: Change Detected
Change Type: New Outbuilding
Detection Method: Aerial Imagery + Object Detection (YOLOv8)
Recommendation: Schedule inspection and update assessed value if necessary.
"""

report_bytes = BytesIO()
report_bytes.write(report_text.encode())
report_bytes.seek(0)

st.download_button(
    label="📄 Download Inspection Report",
    data=report_bytes,
    file_name="inspection_report.txt",
    mime="text/plain"
)

with st.expander("💡 Why Prototype AI Change Detection Tools Internally?"):
    st.markdown("""
**This demo replicates how change detection can be used to identify new construction using aerial imagery and open-source AI tools.**

---

### What This Demo Does

We compare two aerial photographs of the same parcel—one "before" and one "after"—and use object detection (simulated here with a bounding box) to highlight unreported structural changes.

This mimics a real-world process where assessor’s offices compare historical aerial imagery to detect:

- Unreported outbuildings or garages
- Additions to homes
- Barns or sheds on agricultural parcels
- Large-scale grading or land use changes

---

### Where Would the Aerial Imagery Come From?

In real workflows, counties can source aerial images from:

| Source | Frequency | Cost | Notes |
|--------|-----------|------|-------|
| **NAIP** (National Agriculture Imagery Program) | Every 1–3 years | Free | USDA aerial survey, public domain |
| **Google Earth Pro** | On demand | Free | High-resolution imagery available by date |
| **State or local flyovers** | Varies | Varies | Often done by counties or GIS consortiums |
| **Vendors like Nearmap or EagleView** | Up to quarterly | $$$ | Expensive but automated and high-resolution |

For rural counties like Gunnison, **NAIP and Google Earth Pro offer no-cost historical imagery**, which can be downloaded and compared over time.

---

### How AI Helps

With Python + open tools like:

- **Pillow/OpenCV** → image diffing, bounding box highlighting
- **YOLOv8 or Detectron2** → machine learning for object detection
- **GeoPandas** → to connect imagery to parcel boundaries
- **Streamlit** → for internal dashboards and reporting

An assessor's office can:

- Flag parcels with likely changes
- Cross-reference with permits or owner-submitted updates
- Reduce time spent driving out to parcels unnecessarily
- Generate inspection reports for follow-up or audit

---

### Why Build In-House?

Many vendors offer these features—but charge **$10,000–$100,000+ per year**, and still require:

- Setup and training
- Staff adaptation
- System integration

This demo shows how counties can **test and prove value** at little to no cost before investing in full-scale software.

---

> Built entirely with public data, Python, and open-source libraries—this project shows what's possible even in small rural offices with limited budgets.
""")
