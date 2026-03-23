import streamlit as st

# Setup the title for our dream travel app
st.title("🌍 My Future Travel Destinations")

# Initialize the storage for our dream trips
if "destinations" not in st.session_state:
    st.session_state.destinations = []

# Section to add new places
st.header("Add a place to visit")
city = st.text_input("City or Country")
reason = st.text_area("Why do I want to go there?")
image_url = st.text_input("Link to a beautiful photo")

# Save the destination when button is clicked
if st.button("Add to wishlist"):
    if city and reason and image_url:
        st.session_state.destinations.append({
            "place": city,
            "description": reason,
            "image": image_url
        })
        st.success(f"{city} added to the list! Start saving money.")
    else:
        st.warning("Please fill in all the details!")

# Displaying the gallery
st.divider()
for item in st.session_state.destinations:
    col1, col2 = st.columns()
    with col1:
        st.image(item["image"], use_container_width=True)
    with col2:
        st.subheader(item["place"])
        st.write(item["description"])
