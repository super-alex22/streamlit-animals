import streamlit as st

# App title
st.title("🌍 My Future Travel Destinations")

# Initialize the list in session state
if "destinations" not in st.session_state:
    st.session_state.destinations = []

# --- Section to add new places ---
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

# --- Section for destruction ---
if st.session_state.destinations:
    st.divider()
    st.header("Destroy the place") # Epic style preserved
    
    # Use a list comprehension to get all names
    names = [dest["name"] for dest in st.session_state.destinations]
    remove_name = st.selectbox("Choose the place for destruction", names)
    
    if st.button("Remove"):
        for dest in st.session_state.destinations:
            if dest["name"] == remove_name:
                st.session_state.destinations.remove(dest)
                break
        st.success(f"{remove_name} is removed!")
        st.rerun() # Refresh to update immediately

# --- NEW Gallery section ---
st.divider()
st.header("Gallery")
if st.session_state.destinations:
    for destination in st.session_state.destinations:
        st.divider()
        st.subheader(destination["name"]) 
        left_col, right_col = st.columns() 
        
        with left_col:
            st.image(destination["image"], use_container_width=True)

        with right_col:
            st.write("### About this place:")
            st.write(destination["description"])
            st.write("---")
            st.write("### Why I want to go:")
            st.write(destination["reason"])
else:
    st.info("The gallery is empty. Add places!")
