# Preparation and Framing

### Background and context

*What information about your project does the audience need to participate fully in the technical review? You should share enough to make sure your audience understands the questions you are asking, but without going into unnecessary detail.*

We are creating a poker simulator that can play Heads-Up Texas Hold'Em. This is a two-player game where two cards are dealt face down to each player, and then five community cards are dealt face up in three stages. Each player can fold (drop out), raise (increase the bet), check (keep the bet), or call (match the bet of the other player). The simulator will parse poker data (specifically betting amounts, outcomes, and any cards that are shown) and use machine learning to calculate betting strategy based on hand strength and bet amount of other players.

http://www.pokerlistings.com/strategy/headsup-part-1-the-cards-you-play

### Key questions

*What do you want to learn from the review? What are the most important decisions your team is currently contemplating? Where might an outside perspective be most helpful? As you select key questions to ask during the review, bear in mind both the time limitations and background of your audience.*

The best dataset that we could find thus far only has information about player actions and betting amounts; there is no report on who has what cards unless the player chooses to show their hand. Our ability to train the bot on some correlation between hand strength and action/betting amount is therefore highly limited. Should we continue attempting to train a system off of this data set (this likely requires adding more game theory)? Or should we create a bot that plays against an existing online AI (http://www.cleverpiggy.com/nlbot) to generate and train off a more transparent data set?

A key factor in our team’s formation was that we all wanted to learn more about ML, but as such have little prior experience. At this early stage of the project, we have yet to flesh out a lot of the design decisions when it comes to implementing a machine learning algorithm. We are wary of this black box and realize that we will likely face a lot of issues and time sinks along the way. Do you have any additional concerns about things that we are glossing over at this point? Also, if you know about or have resources on machine learning, please let us know!

Do you think it makes sense to have the poker bot as a web-based game? If machine learning does not work, would it work as a web-based game against another human being?

### Agenda for technical review session

*Be specific about how you plan to use your allotted time. What strategies will you use to communicate with your audience?*

We will be spending the first two or three minutes explaining what we envisioned our poker bot to do, while also explaining the game itself briefly in case people don’t know how it’s played. We will then present our current UML diagrams, user interface, layout, etc. from our slideshow. We will be asking questions corresponding to the slides, as well as taking questions, throughout the presentation.
