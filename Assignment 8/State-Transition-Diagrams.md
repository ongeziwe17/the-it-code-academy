# Assignment 8: State Transition Diagrams (Object State Modeling)

## 1. User Account
```mermaid
stateDiagram-v2
    [*] --> Unregistered
    Unregistered --> PendingVerification : register(email, password, role) [email unique]
    PendingVerification --> Active : verifyEmail
    Active --> Suspended : adminSuspend
    Suspended --> Active : adminReactivate
    Active --> Deactivated : deactivateAccount
    Deactivated --> [*]
