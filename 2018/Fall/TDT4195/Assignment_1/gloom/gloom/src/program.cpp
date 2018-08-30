// Local headers
#include "program.hpp"
#include "gloom/gloom.hpp"
#include "gloom/shader.hpp"





void runProgram(GLFWwindow* window)
{
    Gloom::Shader shader;
    shader.makeBasicShader("../gloom/shaders/simple.vert",
                       "../gloom/shaders/simple.frag");

    // Enable depth (Z) buffer (accept "closest" fragment)
    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LESS);

    // Configure miscellaneous OpenGL settings
    glEnable(GL_CULL_FACE);

    // Set default colour after clearing the colour buffer
    glClearColor(0.3f, 0.5f, 0.8f, 1.0f);

    float coords[9] = {
        -0.6, -0.6, 0,
         0.6, -0.6, 0,
         0,    0.6, 0
    };
    // Set up your scene here (create Vertex Array Objects, etc.)

    unsigned int arrayIDs = 0;
    glGenVertexArrays(1, &arrayIDs);
    glBindVertexArray(arrayIDs);
    glGenBuffers(1, &arrayIDs);
    glBindBuffer(GL_ARRAY_BUFFER, arrayIDs);
    glBufferData(GL_ARRAY_BUFFER, 9* sizeof(float), coords, GL_STATIC_DRAW);
    glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,12, 0);
    glEnableVertexAttribArray(0);



    // Generate index buffer
    unsigned int indexes[3] = {0,1,2};
    unsigned int indexIDs = 1;
    glGenBuffers(1, &indexIDs);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indexIDs);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 3*sizeof(unsigned int), indexes, GL_STATIC_DRAW);



    // Rendering Loop
    while (!glfwWindowShouldClose(window))
    {

        // Clear colour and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        shader.activate();
        // Draw your scene here
        glBindVertexArray(arrayIDs);
        glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_INT, 0);

        // Handle other events
        glfwPollEvents();
        handleKeyboardInput(window);
        
        // Deactivate shader program
        shader.deactivate();

        // Flip buffers
        glfwSwapBuffers(window);
    }
    shader.destroy();
}


void handleKeyboardInput(GLFWwindow* window)
{
    // Use escape key for terminating the GLFW window
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
    {
        glfwSetWindowShouldClose(window, GL_TRUE);
    }
}
