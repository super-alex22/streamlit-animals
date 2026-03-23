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
    # We removed the old st.columns(3) that split the whole gallery.
    # Now we process each destination one by one.

    for destination in st.session_state.destinations:
        st.divider() # Visual separator between items
        # Title goes on top for clarity
        st.subheader(destination["name"]) 
        
        # Now we create the two columns for this single item.
        # We make the text column (right) wider than the picture column (left)
        left_col, right_col = st.columns() 
        
        with left_col:
            # Picture on the left.
            st.image(destination["image"], use_container_width=True)

        with right_col:
            # Text on the right. No more "macaroni".
            # We use headings to structure the content.
            st.write(f"### About this place:")
            st.write(destination["description"]) # The long "macaroni" text part
            st.write("---") # Visual horizontal line for structure
            st.write(f"### Why I want to go:")
            st.write(destination["reason"]) # The reason field

else:
    st.info("The gallery is empty. Add places!")
