# Progress Tracker - Associate Data Scientist Bootcamp

**Student**: Md. Ualiur Rahman Rahat  
**Goal**: Complete DataCamp's Assistant Data Scientist Track  
**Started**: April 2026  
**Repository**: [associate-data-scientist-bootcamp](https://github.com/ualiurrahat/associate-data-scientist-bootcamp)

---

## Course 01: Introduction to Python

### ✅ Section 01 - Python Basics (Completed: 2026-04-11)

| #   | File                                | Exercise                    |
| --- | ----------------------------------- | --------------------------- |
| 1   | `01_your_first_python_code.py`      | Your First Python Code      |
| 2   | `02_python_as_a_calculator.py`      | Python as a Calculator      |
| 3   | `03_variable_assignment.py`         | Variable Assignment         |
| 4   | `04_calculations_with_variables.py` | Calculations with Variables |
| 5   | `05_other_variable_types.py`        | Other Variable Types        |
| 6   | `06_operations_with_other_types.py` | Operations with Other Types |

**Key Concepts Learned**:

- `print()` function and basic arithmetic
- Variable assignment and calculations
- Data types: int, float, str, bool
- `type()` function and type behavior differences
- String concatenation vs numeric addition

---

### ✅ Section 02 - Python Lists (Completed: 2026-04-11)

| #   | File                                      | Exercise                          |
| --- | ----------------------------------------- | --------------------------------- |
| 1   | `01_create_a_list.py`                     | Create a List                     |
| 2   | `02_create_lists_with_different_types.py` | Create Lists with Different Types |
| 3   | `03_list_of_lists.py`                     | List of Lists                     |
| 4   | `04_subset_and_conquer.py`                | Subset and Conquer                |
| 5   | `05_slicing_and_dicing.py`                | Slicing and Dicing                |
| 6   | `06_subsetting_lists_of_lists.py`         | Subsetting Lists of Lists         |
| 7   | `07_replace_list_elements.py`             | Replace List Elements             |
| 8   | `08_extend_a_list.py`                     | Extend a List                     |
| 9   | `09_delete_list_elements.py`              | Delete List Elements              |
| 10  | `10_inner_workings_of_lists.py`           | Inner Workings of Lists           |

**Key Concepts Learned**:

- Creating and manipulating lists
- Mixed data types in lists (heterogeneous)
- Nested lists (list of lists for tabular data)
- Indexing: positive (0-based) and negative (from end)
- Slicing: `[start:end]` with exclusive end
- Double indexing for nested lists
- List mutability: replace, extend, delete
- List concatenation with `+` operator
- Reference vs copy semantics (`[:]` for independent copy)

---

### ✅ Section 03 - Functions and Packages (Completed: 2026-04-14)

| #   | File                                | Exercise                                 |
| --- | ----------------------------------- | ---------------------------------------- |
| 1   | `01_familiar_functions.py`          | Familiar Functions                       |
| 2   | `02_help_multiple_arguments.py`     | Help & Multiple Arguments                |
| 3   | `03_string_methods.py`              | String Methods                           |
| 4   | `04_list_methods.py`                | List Methods (`.index()`, `.count()`)    |
| 5   | `05_list_methods_modifying.py`      | List Methods (`.append()`, `.reverse()`) |
| 6   | `06_import_package.py`              | Import Package (`import math`)           |
| 7   | `07_selective_import.py`            | Selective Import (`from math import pi`) |
| 8   | `08_different_ways_of_importing.py` | Different Ways of Importing (aliases)    |

**Key Concepts Learned**:

- Built-in functions: `type()`, `len()`, `int()`, `str()`, `float()`, `bool()`
- `help()` for documentation and understanding arguments
- String methods: `.upper()`, `.count()`
- List methods: `.index()`, `.count()`, `.append()`, `.reverse()`
- Package import patterns: `import math`, `from math import pi`, `import math as m`
- Aliasing with `as` to rename imports
- In-place modification vs returning new objects

---

### ✅ Section 04 - NumPy (Completed: 2026-04-14)

| #   | File                               | Exercise                   |
| --- | ---------------------------------- | -------------------------- |
| 1   | `01_your_first_numpy_array.py`     | Your First NumPy Array     |
| 2   | `02_baseball_players_height.py`    | Baseball Players' Height   |
| 3   | `03_numpy_side_effects.py`         | NumPy Side Effects         |
| 4   | `04_subsetting_numpy_arrays.py`    | Subsetting NumPy Arrays    |
| 5   | `05_your_first_2d_numpy_array.py`  | Your First 2D NumPy Array  |
| 6   | `06_baseball_data_2d_form.py`      | Baseball Data in 2D Form   |
| 7   | `07_subsetting_2d_numpy_arrays.py` | Subsetting 2D NumPy Arrays |
| 8   | `08_2d_arithmetic.py`              | 2D Arithmetic              |
| 9   | `09_average_vs_median.py`          | Average vs Median          |
| 10  | `10_explore_baseball_data.py`      | Explore the Baseball Data  |

**Key Concepts Learned**:

- NumPy arrays vs Python lists (homogeneous, vectorized operations)
- Creating arrays: `np.array()`, `np.arange()`, `np.zeros()`, `np.ones()`
- 2D arrays: list of lists, `.shape` attribute
- Subsetting 1D arrays: indexing and slicing
- Subsetting 2D arrays: `[rows, cols]` syntax with comma
- Vectorized arithmetic: element-wise operations, broadcasting
- Summary statistics: `np.mean()`, `np.median()`, `np.std()`, `np.corrcoef()`
- Outlier detection: comparing mean vs median
- Unit conversion with broadcasting

---

## 📈 Overall Progress

| Course                                  | Status               | Completion Date |
| --------------------------------------- | -------------------- | --------------- |
| 01 - Introduction to Python             | ✅ **100% Complete** | 2026-04-14      |
| 02 - Intermediate Python                | ⏳ Not Started       | -               |
| 03 - Data Manipulation with pandas      | ⏳ Not Started       | -               |
| 04 - Data Visualization with matplotlib | ⏳ Not Started       | -               |
| _More courses to be added_              | ⏳                   | -               |

---

## 📊 Course 01 Statistics

| Section                | Files  | Exercises |
| ---------------------- | ------ | --------- |
| Python Basics          | 6      | 6         |
| Python Lists           | 10     | 10        |
| Functions and Packages | 8      | 8         |
| NumPy                  | 10     | 10        |
| **Total**              | **34** | **34**    |

---

## 📝 Notes

- All code follows PEP 8 standards
- Each file includes encoding, docstring, type hints (no shebang for Windows compatibility)
- "Additional Practice" sections contain self-added exploration
- Commit convention: `feat(course-name): description`
- Repository structure: `XX_course_name/XX_section_name/XX_exercise_name.py`

---

## 🔗 Useful Commands

```bash
# View progress
git log --oneline --graph

# Run a specific exercise
python 01_introduction_to_python/01_python_basics/01_your_first_python_code.py

# Get current status
git status
```
