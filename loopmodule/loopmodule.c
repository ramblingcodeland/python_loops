#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject* loop_run(PyObject* self, PyObject* args) {

    const unsigned long counter_loop_max;
    unsigned long acc = 0;

    if (!PyArg_ParseTuple(args, "k", &counter_loop_max)){
        return NULL;
    }

    for (unsigned long i=1; i < counter_loop_max; i++) {
        acc += i;
    }

    return PyLong_FromLong(acc);

}

static PyMethodDef LoopMethods[] = {
    {"run",  loop_run, METH_VARARGS, "Execute a long loop, accumulating index and returning it."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef loopmodule = {
    PyModuleDef_HEAD_INIT,
    "loop",     /* name of module */
    NULL,       /* module documentation, may be NULL */
    -1,         /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
    LoopMethods
};

PyMODINIT_FUNC
PyInit_loop(void){
    return PyModule_Create(&loopmodule);
}



