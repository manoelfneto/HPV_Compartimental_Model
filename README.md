# HPV_Compartimental_Model

Repository containing a cellular automata made with python using Tkinter trying to simulate a behavior of a infectious disease

This code was made by using Python and a library calling Tkinter to show the interactions between the cells.

**intalling** <br />
first of all you have to install Tkinter, on you terminal type the comand: <br />
pip install Tkinter or automatically by your IDE <br />
**end installing**

This Automata follow some transictions rules to the cells change the states, it is based on the compartimental models and the 8-cell
Moore neighborhood. The cells has 3 states: susceptible (black), infected (yellow) and symptomatic (red).


**Rules to transiction (state 0 to 1):** <br />
If the cell has more than 3 neighbors on state 1 or more than 2 neighbors
on state 2 AND the age of the cell is between 16 and 25, it will get
infected and goes to the state 1.
If the cell has more than 4 neighbors on the state 1 or more than 3
neighbors on the state 2, it will get infected and goes to the state 1.
<br />
**Rule to transiction (state 1 to 2):** <br />
If an organism remain infected for 5 months, it will begin to present
symptoms e goes to the states 2.
<br />
**Rule to transiction (state 2 to 1):**
If the infect time of the cell is more than 8, it goes back to the state 1.

