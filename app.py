import streamlit as st

st.title("🌍 My Future Travel Destinations")

if "destinations" not in st.session_state:
    st.session_state.destinations = []

st.header("Add a place to visit")
city = st.text_input("City, Country or Place")
reason = st.text_area("Why do I want to go there?")
description = st.text_area("What is the place like?")
image_url = st.text_input("Link to a beautiful photo")

if st.button("Add to wishlist"):
    if city and reason and image_url:
        st.session_state.destinations.append({
            "name": city,
            "description": description,
            "reason": reason,
            "image": image_url
        })
        st.success(f"{city} added to the list! Start saving money.")
    else:
        st.warning("Please fill in all the details!")

if st.session_state.destinations:
    st.divider()
    st.header("Destroy the place") 
    
    names = [dest["name"] for dest in st.session_state.destinations]
    remove_name = st.selectbox("Choose the place for destruction", names)
    
    if st.button("Remove"):
        for dest in st.session_state.destinations:
            if dest["name"] == remove_name:
                st.session_state.destinations.remove(dest)
                break
        st.success(f"{remove_name} is removed!")
        st.rerun() # Refresh to update the gallery immediately

st.divider()
st.header("Gallery")
if st.session_state.destinations:
    cols = st.columns(3)
    for idx, destination in enumerate(st.session_state.destinations):
        with cols[idx % 3]:
            st.subheader(destination["name"])
            st.image(destination["image"], use_container_width=True)
            st.write(f"**About:** {destination['description']}")
            st.write(f"**Reason:** {destination['reason']}")
else:
    st.info("The gallery is empty. Add places!")
