# Reflection and Synthesis

### Feedback and decisions

*Based upon your notes from the technical review, synthesize the feedback you received addressing your key questions. How do you plan to incorporate it going forward? What new questions did you generate?*

One of our key questions going into the Architectural Review was to what extent we should train off of an existing dataset as opposed to have the bot learn from scratch. Paul’s recommendation to move forward with reinforcement learning has become our primary focus in the next sprint. We are basing further research on different reinforcement learning paradigms, in attempt to flesh out some of the ambiguity in the “A.I. part” of our project (another key concern we heard relayed back from the class).

However, Paul also raised an additional question for our group to consider, which is how we will develop a comprehensive model of an opponent, if we do so at all. What level and how much information will our starter opponent possess?

With this data to ML pivot, we have also significantly cut back on the time we need to spend text mining/parsing through online datasets. This shift is in line with our learning goals of wanting to experiment with machine learning. Shedding some of the work around data parsing and working to simplify the game play will allow to focus more on our goals.

Another question we had was whether our poker simulation would work as a web-based game. Patrick and Katie were listed as people to consult with for more information on web-based apps. It could work with flask and HTML, but with our MVC model, it would have to refresh or link to a new page with the update every time a new action is performed. As a result, we will be training the bot offline while developing the web app with graphics separately.

### Review process reflection

*How did the review go? Did you get answers to your key questions? Did you provide too much/too little context for your audience? Did you stick closely to your planned agenda, or did you discover new things during the discussion that made you change your plans? What could you do next time to have an even more effective technical review?*

We stuck to our agenda, which was to give background information on how to play Heads-Up Texas Hold’em, before going into what we have done so far and decisions we are looking at, with room for questions and feedback at the end. The extended time for class interaction and feedback was really helpful to us, as we planned our presentation to mostly be background and contextual information. We received a lot of useful information regarding our key questions, but it may have been helpful to have more explicit questions. Our questions might have seemed too open-ended or broad, which resulted in feedback that pointed us in the same direction we were looking at and served as leading questions.  A more effective technical review would probably contain more questions with higher specificity.
