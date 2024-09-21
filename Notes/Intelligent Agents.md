## Agents
___
An **agent** is anything that can be viewed as perceiving its environment through **sensors** and acting upon that environment through **actuators**. A human has its eyes, ears, and touch as **sensory** tools and hands, legs as **actuators**. A robotic agent might have cameras and infrared range finders for sensors and various motors for actuators. A **rational agent** is one that does the right thing—conceptually speaking, every entry in the table for the agent function is filled out correctly. The **agent function** for an agent specifies the action taken by the agent in response to any percept sequence. 

The definition of a rational agent is: For each possible percept sequence, a rational agent should select an action that is expected to maximize its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge the agent has.

A task environment specification includes the performance measure, the external environment, the actuators, and the sensors. In designing an agent, the first step must always be to specify the task environment as fully as possible.
## Task Environments - Dimensions
___
**Fully Observable vs Partially Observable:** 
- If an agent's sensors give it access to the complete state of the environment at each point in time, then the task environment is fully observable. 
- Fully observable environments are convenient because the agent need not maintain any internal state to keep track of the world. 

**Single agent vs Multi-agent:**
- In chess (multi-agent), the distinction is whether a player's behavior is best described as maximizing a performance whose value depends on the opponent's behavior. Therefore, chess is a **competitive** multi-agent environment. 
- In the taxi-driving environment, avoiding collisions maximizes the performance measure of all agents, so it's a partially **cooperative** multi-agent environment. 

**Deterministic vs Stochastic:**
- If the next state of the environments is completely determined by the current state and the action executed by the agent, then it's a deterministic environment
-  Stochastic environments are uncertain about outcomes is quantified in terms of probability. Nondeterministic environment is one in which actions are characterized by their possible outcomes but no probabilities are attached to them.  

**Episodic vs Sequential:**
- Episodic task environment is divided into atomic episodes. Each episode the agent receives a percept and then performs a single action. The next episode does not depend on the actions taken in the previous episode.
- Chess and Taxi Driving is **sequential**. 

**Static vs Dynamic:**
- Environment can change while an agent is deliberating then the environment is **dynamic** for that agent. e.g. Taxi Driving
- **Static** environments are easy to deal with because the agent need not keep looking at the environment to perform the next set of actions. e.g. Crossword Puzzles

**Discrete vs Continuous:**
- The discrete/continuous distinction applies to the state of the environment, to the way time is handled, and to the percepts and actions of the agent.
- Chess environment has a finite number of distinct states (not the clock). Chess also has a **discrete** set of percepts and actions.
- Taxi driving is a **continuous-state** and **continuous-time** problem 

**Known vs Unknown:**
- This distinction refers not to the environment itself but to the agent's state of knowledge of the environment. 
- In a **known** environment, the outcomes (or outcome probabilities if the environment is stochastic) for all actions are given.
- If the environment is **unknown**, the agent will have to learn how it works in order to make good decisions.

![[Figure 2.6Task Environments Examples.png]]

## Structure of Agents
___
The AI is to design an **agent program** that implements the **agent function** - the mapping from percepts to actions. 
$$agent =architecture +program$$
**Simple Reflex Agents:**
- Select actions on basis of the current percept ignoring the rest of the percept history
- Respond directly to percepts
![[Figure 2.9 Simple Reflex Agent.png| 400]]

**Model-Based Reflex Agents:**
- To handle **partial observability** is for the agent to track of the part of the world it can't see now. The agent should maintain some sort of **internal state** that depends on the percept history. 
- This knowledge about “how the world works”—whether implemented in simple Boolean circuits or in complete scientific theories—is called a model of the world. An agent that uses such a model is called a **model-based agent**.

![[Figure 2.11 A model-based reflex agent.png| 400]]

**Goal-Based Agents:**
- As well as a current state description, the agent needs some sort of **goal** information that describes situations that are desirable.
- Search and Planning are the subfields of AI devoted to finding action sequences that achieve that agent's goals. 
![[Figure 2.13 A model,goal-based agent.png| 400]]

**Utility-Based Agents**
- Goals alone are not enough to generate high-quality behaviors in most environments. Therefore, a general performance measures should allow a comparison using **utility**.
- An agent's **utility function** is the internalization of the performance measure.
- When there are conflicting goals, some of which can be achieved , the utility function specifies the tradeoffs needed.
![[Figure 2.14 Utility-Based Agents.png| 400]]

**Learning Agents:**
- **Learning Element** is responsible for making improvements. It uses feedback from the **critic** on how the agent is doing and determines how the performance element should be modified to do better in the future. 
- **Performance element** is responsible for selecting external actions. 
- **Problem Generator** is the last element of a learning agent. It is responsible for suggesting actions that will lead to new and informative experiences. 
![[Figure 2.15 A general learning agent.png| 400]]


### Components of Agent Programs
____
![[Atomic-Factored-Structured.png]]

**Atomic Representation**: each state of the world is indivisible. There is no internal structure. It reduces the state of the world to a block box. Algorithms like **[[Search]]** and **Game-Playing**, **Hidden Markov Models**, and **Markov Decision Processes** all use the atomic representations.  

**Factored Representation** splits up each state into a fixed set of **variables/attributes**, each of which can have a **value**. While the atomic states are just black boxes (nothing in common), two different factored states can share some *attributes*. Algorithms that use this representation are **Constraint satisfaction**, **propositional logic,** **planning**, **Bayesian networks**, and **machine learning algorithms**. 

**Structured Representation** have various and varying relationships that can be described explicitly. Structured representations underlie **relational databases** and **first-order logic**, **first-order probability models**, **knowledge-based learning** and much of **natural language understanding**. In fact, almost everything that humans express in natural language concerns objects and their relationships.

From atomic to structured representation, the **expressiveness** increases. The more expressive the more concise. 