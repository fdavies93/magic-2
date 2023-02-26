* Make code more resilient and improve code completion by using fewer generic types
  * Refactor context to a (non-abstract) base class (instead of kwargs dict) and let specific calls to Events.fire_event extend that class.
  * Refactor component to an abstract class and let specific components extend that class - like Unity's MonoBehaviour.
* 