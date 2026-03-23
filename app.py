import streamlit as st

st.title("🌍 My Future Travel Destinations")

if "destinations" not in st.session_state:
    st.session_state.destinations = []

# Section to add new places
st.header("Add a place to visit")
city = st.text_input("City, Country or Place")
reason = st.text_area("Why do I want to go there?")
description = st.text_area("Why is the place like?")
image_url = st.text_input("Link to a beautiful photo")

# Save the destination when button is clicked
if st.button("Add to wishlist"):
    if city and reason and image_url:
        st.session_state.destinations.append({
            "place": city,
            "description": description,
            "reason": reason,
            "image": image_url
        })
        st.success(f"{city} added to the list! Start saving money.")
    else:
        st.warning("Please fill in all the details!")

if st.session_state.destinations:
    st.header("Destroy the place")
    names = []
    for a in st.session_state.destinations:
        names.append(a["name"])
    remove_name = st.selectbox("Choose the place for destroyment", names)
    if st.button("Remove"):
        for a in st.session_state.destinations:
            if a["name"] == remove_name:
                st.session_state.destinations.remove(a)
                break
        st.success(f"{remove_name} is removed!")
st.header("Gallery")
if st.session_state.destinations:
    cols = st.columns(3)
    for idx, destination in enumerate(st.session_state.animals):
        with cols [idx % 3]:
            st.subheader(destination["name"])
            st.image(destination["image"], use_column_width= True)
            st.write(animal["description"])
else:
    st.info("The gallery is empty. Add places!")
