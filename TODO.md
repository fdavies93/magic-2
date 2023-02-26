* Make code more resilient and improve code completion by using fewer generic types
  * Refactor context to a (non-abstract) base class (instead of kwargs dict) and let specific calls to Events.fire_event extend that class.
  * Refactor component to an abstract class and let specific components extend that class - like Unity's MonoBehaviour.
* Figure out a project structure / package management solution such that the following use cases can be kept separate (most likely symlink-based rather than submodules):
  * Local text adventure running only on local machine
  * Server-client MUD, whether running locally or over network
  * Graphical demo using PyGame