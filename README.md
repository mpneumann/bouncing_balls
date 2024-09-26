# bouncing_balls
bouncing balls game 

Window:
- Functionality: display a window with the balls
- Inputs: none 
- Outputs: render the balls and update their positions every frame with smooth animations.
User Controls:
- Init/End Control:
    - Functionality: key input will start or stop the ball movement.
    - Inputs: a designated key 
    - Outputs:
        - Start: the balls begin moving.
        - Stop: the balls freeze in their current position.
- Quantity Control:
    - Functionality: input field to change ball quantity 
    - Inputs: user can input the number of balls in an empty field
    - Outputs: changing balls dynamically
- Speed Control:
    - Functionality: slider to adjust speed 
    - Inputs: user moves the slider to change speed.
    - Outputs: balls change speed real time 
Animations:
- Color Variation:
    - Functionality: there are variations in ball color choosing from a set of ball colors 
    - Inputs: none
    - Outputs: the balls maintained their assigned color 
- Size Variation:
    - Functionality: the balls have differing sizes 
    - Inputs: none
    - Outputs: the window displays the balls of different sizes 
- Antigravity Mode:
    - Functionality: the balls will bounce the opposite direction of which they previously bounced 
    - Inputs: a timer cutdown
    - Outputs: the window displays balls bouncing the opposite direction
- Collision:
    - Functionality: balls bounce off each other 
    - Inputs: none
    - Outputs: balls reflect Newton's Third Law 
Performance:
- Smooth Animation:
    - Functionality: no frame rate drops despite many balls 
    - Inputs: regular updating of movement and ball count 
    - Outputs: the balls move fluidly without lag
- Scalability
    - Functionality: able to handle an increasing number of balls without compromising performance.
    - Inputs: the system should adjust its memory based on the number of balls 
    - Outputs: rendering works up to a large limit of balls 
