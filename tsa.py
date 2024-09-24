import streamlit as st

st.set_page_config(page_title="WATCHDOG", page_icon=":rolling_on_the_floor_laughing", layout="wide")
st.subheader("WATCHDOG")
st.write("---")
left_column, right_column = st.columns(2)
with left_column:
    st.header("The Idea")
    st.write(
        """
        We made WATCHDOG as a project for TSA (Technology Student Association)
         and our prompt was an invention that promotes
         school safety. We had gone through countless ideas of weapons, and
          systems until we landed on ideas such as diabetes. We learned that
          diabetes was a rising issue and we wanted to help solve it. We had
           decided this was it. Our idea was to make an application
           that could tell students how many carbs were in their meals so the
            school nurse could input the numbers into the doctor's
            formula and administer insulin. It was genius.
        """
    )

st.write("---")
left_column, right_column = st.columns(2)
with left_column:
    st.header("The Code")
    st.write(
        """
        We ended up writing the code in code.org's version of javascript. It may have been a little weird, but it worked.
         It took three days of constant work to finish the base code but it worked. This base code is what we took to the regional competition.
        """
    )

    st.write("---")
    with left_column:
        st.header("The Models & Displays")
        st.write(
            """
            Our models went through around 3 iterations each time immensely improving. We modeled a phone because that
             is were our app would be used. We laminated screenshots of our applications pages to demonstrate how the
              app worked. We also made a tri fold display. This was completed in a blue and orange color way and it looked
               amazing. We had paragraphs of information which we ended up using on our second board as well.
            """
        )

        st.write("---")
        with left_column:
            st.header("Did We Win?")
            st.write(
                """
                We were so excited yet nervous, we had just finished studying for our presentation to the judges after we had made
                 it to the seminfinal rounds. We had walked into the room and showed the judges our display. We had all forgotten about
                  script but we played it by ear. We were so scared we just sat outside for around 10 minutes after the fact. On the last
                   night of the competition we had all attended the award ceremony. We had been waiting for about one hour but eventually
                   , we heard it. WE HAD ACHIEVED FIRST PLACE! We were all so excited. We knew we were then going to attend the national
                    competition later that year.
                """
            )

            st.write("---")
            with left_column:
                st.header("Nationals")
                st.write(
                    """
                    The national competition was cool. It was in a fancy Orlando hotel. We had all driven out there and met up together.
                     We were all very confident and we turned our project in filled with the relief yet scared about if we were going to make semifinals.
                      We were all crushed when we heard we did not. We were told our project did not show school safety yet we all knew it did.
                       We plan to make the project even better and release it int o the real world. We know we will make school safer.
                    """
                )

st.write("[WATCHDOG >](https://studio.code.org/projects/applab/q0KpiatHN_CDF9UZW3RcrZJb_V7wp2Ckei10XpppkNY)")
