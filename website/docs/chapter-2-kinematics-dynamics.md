## Chapter 2: Kinematics and Dynamics of Humanoid Robots

## Table of Contents

*   [Introduction to Humanoid Robotics](#introduction-to-humanoid-robotics)
*   [Kinematics](#kinematics)
    *   [Forward Kinematics](#forward-kinematics)
    *   [Inverse Kinematics](#inverse-kinematics)
*   [Jacobian Matrix](#jacobian-matrix)
    *   [Significance](#significance)
    *   [Singularities](#singularities)
*   [Dynamics](#dynamics)
    *   [Lagrangian Formulation](#lagrangian-formulation)
    *   [Newton-Euler Formulation](#newton-euler-formulation)
*   [Trajectory Generation](#trajectory-generation)
    *   [Joint Space vs. Task Space Trajectories](#joint-space-vs-task-space-trajectories)
    *   [Polynomial Trajectories](#polynomial-trajectories)
*   [Balance Control (Zero Moment Point - ZMP)](#balance-control-zero-moment-point---zmp)
    *   [Concept of ZMP](#concept-of-zmp)
    *   [Static and Dynamic Stability](#static-and-dynamic-stability)
    *   [ZMP Control for Walking](#zmp-control-for-walking)
*   [Examples and Exercises](#examples-and-exercises)
*   [Summary](#summary)

### 1. Introduction to Humanoid Robotics

Humanoid robots are complex systems designed to mimic human form and movement. To understand and control these robots, a deep understanding of their kinematics and dynamics is essential. Kinematics describes the geometry of motion without considering the forces causing it, focusing on the relationship between joint angles and the robot's end-effector positions. Dynamics, on the other hand, deals with the forces and torques that produce motion, analyzing the relationship between forces, mass, and acceleration. This chapter will delve into these fundamental concepts, crucial for designing, simulating, and controlling humanoid robots.

### 2. Kinematics

Kinematics in robotics involves describing the position and orientation of the robot's links and end-effectors relative to a fixed base frame.

#### 2.1. Forward Kinematics

Forward kinematics is the process of calculating the position and orientation of the end-effector given the values of all joint variables (angles for revolute joints, displacements for prismatic joints).

The most common method for representing the kinematic chain of a robot is the Denavit-Hartenberg (D-H) parameter convention. Each link is assigned a coordinate frame, and the relationship between consecutive frames is described by four D-H parameters:

*   **`a_i`**: The length of the common normal between `Z_i` and `Z_{i-1}` axes.
*   **`α_i`**: The angle from `Z_{i-1}` to `Z_i` about the common normal.
*   **`d_i`**: The distance along the `Z_{i-1}` axis from the origin of frame `i-1` to the common normal.
*   **`θ_i`**: The angle from `X_{i-1}` to `X_i` about the `Z_i` axis.

A homogeneous transformation matrix `A_i^{i-1}` describes the transformation from frame `i` to frame `i-1`:

```
A_i^{i-1} = [cos θ_i   -sin θ_i cos α_i   sin θ_i sin α_i   a_i cos θ_i]
            [sin θ_i    cos θ_i cos α_i   -cos θ_i sin α_i   a_i sin θ_i]
            [   0           sin α_i           cos α_i           d_i    ]
            [   0             0                 0               1    ]
```
For a robot with `n` joints, the transformation from the base frame (0) to the end-effector frame (`n`) is given by the product of individual transformation matrices:

```
T_n^0 = A_1^0 A_2^1 ... A_n^{n-1}
```
#### 2.2. Inverse Kinematics

Inverse kinematics (IK) is the reverse problem: determining the joint variables required to achieve a desired end-effector position and orientation. This is significantly more challenging than forward kinematics, as analytical solutions exist only for simpler robot configurations (e.g., 3-DOF manipulators, or those satisfying Paden-Kahan sub-problems).

For humanoid robots with many degrees of freedom and complex link structures, numerical methods are often employed. These iterative methods typically involve minimizing an error function between the current end-effector pose and the desired pose. Common numerical techniques include:

*   **Jacobian-based methods**: Using the inverse of the Jacobian matrix to calculate joint velocity adjustments.
*   **Optimization-based methods**: Formulating IK as an optimization problem where joint angles are varied to minimize a cost function (e.g., squared error of position and orientation).

The main challenges in inverse kinematics include:
*   **Multiple solutions**: There might be several joint configurations for a single end-effector pose.
*   **No solution**: The desired pose might be outside the robot's workspace.
*   **Singularities**: Certain joint configurations where the robot loses one or more degrees of freedom, making the Jacobian matrix singular.

### 3. Jacobian Matrix

The Jacobian matrix (J) is a fundamental tool in robotics that relates joint velocities to end-effector velocities (both linear and angular). It provides a linearized mapping between the joint space and the task space.

For an `n`-DOF robot, if `q̇` is the vector of joint velocities and `ẋ` is the vector of end-effector velocities (linear and angular), then:

```
ẋ = J(q) q̇
```
Where `q` is the vector of joint variables.

The Jacobian matrix can be partitioned into a linear velocity Jacobian (`J_v`) and an angular velocity Jacobian (`J_ω`):

```
J = [J_v]
    [J_ω]
```
Each column of the Jacobian corresponds to a joint. For a revolute joint `j`, the `j`-th column is:

```
[(z_{j-1} × (p_n - p_{j-1})) ]
[         z_{j-1}          ]
```
Where `z_{j-1}` is the `Z`-axis of frame `j-1`, `p_n` is the position of the end-effector, and `p_{j-1}` is the position of the origin of frame `j-1`.

#### 3.1. Significance

The Jacobian matrix is crucial for:
*   **Velocity kinematics**: Mapping joint velocities to end-effector velocities.
*   **Inverse kinematics**: Used in numerical methods to find joint angle changes for desired end-effector movements.
*   **Force mapping**: Relating forces/torques in the task space to torques in the joint space (via `τ = J^T F`).
*   **Singularity analysis**: Identifying configurations where the robot loses dexterity.

#### 3.2. Singularities

Singularities occur when the Jacobian matrix loses full rank, meaning it cannot be inverted. At these configurations, the robot loses one or more degrees of freedom in its task space, making it unable to move its end-effector in certain directions, even with non-zero joint velocities.

Common types of singularities include:
*   **Boundary singularities**: Occur when the robot reaches the limits of its workspace (e.g., fully extended arm).
*   **Wrist singularities**: Occur when the wrist joints align, causing a loss of orientation control.

Avoiding singularities is a critical aspect of robot motion planning and control.

### 4. Dynamics

Robot dynamics describes the relationship between the forces and torques applied to a robot and the resulting motion. It is essential for trajectory tracking, force control, and understanding energy consumption.

The general form of the dynamic equation for an `n`-DOF robot is:

```
M(q)q̈ + C(q, q̇)q̇ + G(q) = τ
```
Where:
*   `M(q)` is the `n × n` mass matrix (or inertia matrix).
*   `C(q, q̇)q̇` represents Coriolis and centrifugal forces.
*   `G(q)` represents gravitational forces.
*   `τ` is the vector of joint torques.
*   `q`, `q̇`, `q̈` are joint position, velocity, and acceleration vectors, respectively.

There are two primary approaches to deriving the dynamic equations: Lagrangian formulation and Newton-Euler formulation.

#### 4.1. Lagrangian Formulation

The Lagrangian formulation is an energy-based method. It starts with scalar energy functions for the entire system, making it generally simpler for theoretical analysis and understanding the overall system behavior.

The Lagrangian $L$ is defined as the difference between the kinetic energy ($K$) and potential energy ($P$) of the system:

```
L(q, q̇) = K(q, q̇) - P(q)
```

Lagrange's equations are then used to derive the equations of motion:

```
d/dt(∂L/∂q̇_i) - ∂L/∂q_i = τ_i
```

Where `τ_i` is the generalized force (torque) at joint `i`.

**Advantages:**
*   Systematic and scalar-based, easier to manage for complex systems conceptually.
*   Automatically accounts for constraints if generalized coordinates are chosen properly.

**Disadvantages:**
*   Computationally intensive for real-time control due to the calculation of partial derivatives and integrals.
*   Less intuitive for understanding individual forces and torques acting on links.

#### 4.2. Newton-Euler Formulation

The Newton-Euler formulation is a force-based method that applies Newton's second law and Euler's equation of motion (for rigid bodies) to each link sequentially, from the base to the end-effector (forward recursion) and then from the end-effector back to the base (backward recursion).

**Forward Recursion (from base to end-effector):**
*   Calculate linear and angular velocities and accelerations for each link.
*   Calculate the center of mass linear acceleration for each link.

**Backward Recursion (from end-effector to base):**
*   Calculate the forces and moments acting on each link.
*   Calculate the joint torques/forces.

**Advantages:**
*   More intuitive for understanding the physical forces and moments acting on each link.
*   Computationally efficient for inverse dynamics (calculating torques given motion).
*   Suitable for real-time control applications.

**Disadvantages:**
*   More complex to derive for large systems compared to the Lagrangian approach.
*   Requires careful bookkeeping of reference frames and vector transformations.

### 5. Trajectory Generation

Trajectory generation is the process of planning a path for the robot to follow, including its position, velocity, and acceleration profiles over time. This is critical for smooth, efficient, and safe robot motion.

#### 5.1. Joint Space vs. Task Space Trajectories

*   **Joint Space Trajectories**:
    *   Planned directly in the joint variable space ($q$).
    *   Easier to ensure joint limits and velocity/acceleration limits are respected.
    *   Can lead to non-straight-line paths in Cartesian space, which might not be desirable for certain tasks.
    *   Typically uses cubic or quintic polynomials to generate smooth position, velocity, and acceleration profiles between waypoints.

*   **Task Space Trajectories (Cartesian Space Trajectories)**:
    *   Planned in the end-effector's Cartesian space (position and orientation).
    *   Requires inverse kinematics to convert Cartesian waypoints into joint angles.
    *   Ensures a straight-line path in Cartesian space, which is often intuitive for tasks.
    *   Can violate joint limits or result in undesirable joint velocities/accelerations if not carefully managed.

#### 5.2. Polynomial Trajectories

Cubic and quintic polynomials are commonly used for trajectory generation due to their ability to provide smooth transitions between waypoints.

*   **Cubic Polynomials**:
    *   Require two boundary conditions (e.g., initial and final position, and initial and final velocity).
    *   The acceleration profile will be discontinuous at waypoints.

*   **Quintic Polynomials**:
    *   Require three boundary conditions (e.g., initial and final position, velocity, and acceleration).
    *   Produce continuous acceleration profiles, resulting in smoother motion and reduced jerks. This is often preferred for humanoid robots to prevent sudden impacts and ensure balance.

### 6. Balance Control (Zero Moment Point - ZMP)

Maintaining balance is a paramount challenge for humanoid robots, especially during walking or performing dynamic tasks. The Zero Moment Point (ZMP) is a crucial concept for achieving stable locomotion.

#### 6.1. Concept of ZMP

The Zero Moment Point (ZMP) is a point on the ground (or support surface) where the net moment of all active forces (gravity, inertial forces) acting on the robot is zero. If the robot is to remain stable (not tip over), its ZMP must stay within the boundaries of its support polygon (the convex hull of all contact points with the ground).

Mathematically, the ZMP can be derived from the dynamic equations by setting the sum of all moments about the ZMP to zero.

#### 6.2. Static and Dynamic Stability

*   **Static Stability**: A robot is statically stable if its center of mass (CoM) projection lies within its support polygon. This is applicable for very slow movements or standing.
*   **Dynamic Stability**: For walking and dynamic movements, relying solely on static stability is insufficient. Dynamic stability, often quantified by the ZMP, accounts for inertial forces. A robot is dynamically stable if its ZMP remains within the support polygon throughout its motion.

#### 6.3. ZMP Control for Walking

ZMP-based control strategies are widely used for generating stable walking gaits for humanoid robots. The general idea is to plan a desired ZMP trajectory (which stays within the support polygon) and then generate the corresponding robot motion (CoM trajectory and joint angles) that produces this ZMP.

A common approach involves:
1.  **ZMP Trajectory Planning**: Define a sequence of ZMP points that ensure stability during different phases of walking (single support, double support).
2.  **CoM Trajectory Generation**: Use simplified models (e.g., Linear Inverted Pendulum Model - LIPM) to generate a CoM trajectory that achieves the desired ZMP.
3.  **Inverse Kinematics**: Calculate the joint angles required to realize the CoM and foot trajectories.
4.  **Dynamics and Control**: Use dynamic models to calculate joint torques and implement feedback control to track the planned trajectories, often using a Proportional-Derivative (PD) controller.

Challenges in ZMP control include robustly handling external disturbances, uneven terrain, and computational complexity for real-time implementation.

### 7. Examples and Exercises

#### Example: Forward Kinematics (2-DOF Planar Arm)

Consider a 2-DOF planar robot arm with two revolute joints.
*   Link 1 length: `L_1`
*   Link 2 length: `L_2`
*   Joint 1 angle: `θ_1` (relative to X-axis)
*   Joint 2 angle: `θ_2` (relative to Link 1)

**Solution:**
The position of the end-effector (`x_e`, `y_e`) can be found using trigonometry:
`x_e = L_1 cos(θ_1) + L_2 cos(θ_1 + θ_2)`
`y_e = L_1 sin(θ_1) + L_2 sin(θ_1 + θ_2)`

#### Exercise 1: Inverse Kinematics (2-DOF Planar Arm)

For the same 2-DOF planar arm, given a desired end-effector position (`x_d`, `y_d`), find the joint angles `θ_1` and `θ_2`.

**Hint:** Use the Law of Cosines to find `θ_2` first, then `θ_1`. Consider multiple solutions.

#### Exercise 2: Jacobian Matrix (2-DOF Planar Arm)

Calculate the Jacobian matrix for the 2-DOF planar arm, relating joint velocities to end-effector linear velocities. Identify any singular configurations.

#### Exercise 3: Trajectory Generation

A robot's joint needs to move from an initial position of `0` radians to a final position of `π/2` radians in `2` seconds. The initial and final velocities are `0` rad/s. Generate a cubic polynomial trajectory for this joint. Calculate the position, velocity, and acceleration at `t=1` second.

### 8. Summary

Kinematics and dynamics are foundational pillars for understanding and controlling humanoid robots. Forward kinematics allows us to determine the end-effector pose from joint angles, while inverse kinematics solves the more complex problem of finding joint angles for a desired end-effector pose. The Jacobian matrix is vital for relating velocities between joint and task spaces, and for analyzing singularities where the robot loses dexterity.

Robot dynamics, described by formulations such as Lagrangian and Newton-Euler, provides the relationship between forces/torques and motion, essential for precise control and simulation. Finally, trajectory generation ensures smooth and efficient movement, while balance control, particularly through the Zero Moment Point (ZMP) concept, enables stable locomotion for complex bipedal robots. Mastering these concepts is crucial for the advancement and practical application of humanoid robotics.
