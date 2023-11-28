# RISE_Tests

## Why

In the Open Education Platform (OPE), Jupyter Lab serves as the primary user interface. Rigorous testing is essential for data processing accuracy and reliability, essential for research and analytical workflows. By testing Jupyter Notebooks, we ensure that all functionalities, including code cell execution, operate correctly and integrate seamlessly with various tools and libraries across different platforms.

Additionally, OPE employs RISE to convert Jupyter notebooks into slideshows, enhancing interactive presentations. This feature is widely used in educational and professional settings for presenting complex data and analyses. Testing RISE is crucial to verify that it operates as intended and ensures that these presentations are reliable and effective in conveying information accurately.

Overall, comprehensive testing of both Jupyter Notebooks and RISE is integral to maintain the platform's effectiveness and reliability.

## What

1. **Jupyter Notebook Testing:**

- - The testing process for Jupyter Notebooks includes confirming the correct installation of specific versions and validating that all code cells execute without errors.
  - Testing extends to verifying users' ability to install packages via `pip`.
  - Verifying users have the necessary permissions to access Conda functionalities is essential.

2. **RISE Functionality Testing:**

- - **Content Integrity and Visual Accuracy:** Verifying that the content's integrity is maintained during its conversion from a notebook to a slideshow and that visual outputs are accurately displayed. This is essential for ensuring that the presentations effectively and accurately convey information.
  - **Interactive Feature Verification:** Since RISE supports interactive elements like real-time code execution, testing these features is crucial to ensure smooth functionality during presentations.
  - **Compatibility and Stability:** RISE testing includes examining compatibility with different versions of Jupyter and assessing stability during operation. This step is vital to avoid potential issues arising from version mismatches or operational instabilities.
  - **Error-Free Operation:** All elements within RISE must operate without errors to guarantee a practical and seamless learning experience.

Overall, thorough testing of Jupyter Notebook installations and RISE functionalities is integral to maintaining the high standards of reliability and efficiency in the Open Education Platform.

## How

### Set up RISE on Jupyter Lab

In the [Dockerfile](https://github.com/OPEFFORT/OPE-Testing/blob/5df4c895e9e30ee24b36a4b295a5a9613d7853d4/base/Dockerfile#L49C6-L49C6) ,`jupyterlab-rise` is installed directly using pip with the command `pip install jupyterlab_rise`.

### Test Jupyter Installation

To ensure that all necessary libraries and dependencies are correctly installed, we use a Jupyter notebook instance. The test ensures that all required imports in the Jupyter notebook instance are installed and functioning without errors.

### Test RISE Functionality

We employ Selenium for the RISE test to simulate opening a Jupyter Notebook file. The test then captures screenshots to confirm the correct functioning of RISE and visually verify its performance within a Jupyter environment.

#### Test with locally

To effectively test RISE functionality within Jupyter Lab, our process involves the following steps:

1. **Retrieve Jupyter Lab Token:** First, obtain a `token` from a Jupyter Lab instance.
<<<<<<< HEAD:tests/Rise_Tests.md
   ![Screenshot 2023-11-27 at 14 56 42](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/9c699718-6393-4596-b13a-a8bef8cd086c)

2. **Execute RISE Test Script:** Run the command `python rise-test.py {token}`. This command initiates the opening of the Jupyter Lab instance and captures a screenshot of the launcher page.
   ![Screenshot 2023-11-27 at 15 11 20](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/3a9a9cb2-4f89-4b08-8fe5-94be837e03ad)

   If you are using the Jupyter notebook version, named `run_rise_test.ipynb`, simply replace `{token}` with your specific token and then proceed to execute the cells within the notebook.

   ![Screenshot 2023-11-27 at 15 23 04](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/577249e3-7c97-4344-8e86-0a7352e6d619)

3. **Create and Capture Notebook File:** Following the simulated click on the Notebook launch icon, a new Jupyter Notebook file is automatically created.. We then take a screenshot for comparison purposes.
   ![new_nb_screenshot](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/78c9470a-eff9-4ec0-b3ab-94eaeaa7afbf)

4. **Activate and Document RISE Function:** The test proceeds to locate and double-click the RISE icon, triggering the RISE function. A screenshot is taken at this stage to document the functionality.
   ![rise_screenshot](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/26f8a25b-6574-4ba3-9ddf-e341539e0c0a)
=======
![Screenshot 2023-11-27 at 14 56 42](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/9c699718-6393-4596-b13a-a8bef8cd086c)


2. **Execute RISE Test Script:** Run the command `python rise-test.py {token}`. This command initiates the opening of the Jupyter Lab instance and captures a screenshot of the launcher page.
![Screenshot 2023-11-27 at 15 11 20](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/3a9a9cb2-4f89-4b08-8fe5-94be837e03ad)

    If you are using the Jupyter notebook version, named `run_rise_test.ipynb`, simply replace `{token}` with your specific token and then proceed to execute the cells within the notebook.

>>>>>>> origin/container-base-ope:tests/rise-test.md

   ![Screenshot 2023-11-27 at 15 23 04](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/577249e3-7c97-4344-8e86-0a7352e6d619)


4. **Create and Capture Notebook File:** Following the simulated click on the Notebook launch icon, a new Jupyter Notebook file is automatically created.. We then take a screenshot for comparison purposes.
![new_nb_screenshot](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/78c9470a-eff9-4ec0-b3ab-94eaeaa7afbf)


5. **Activate and Document RISE Function:** The test proceeds to locate and double-click the RISE icon, triggering the RISE function. A screenshot is taken at this stage to document the functionality.
![rise_screenshot](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/26f8a25b-6574-4ba3-9ddf-e341539e0c0a)



6. **Test Fullscreen Feature:** The process includes searching for and activating the fullscreen button to display the slideshow in fullscreen mode.

<<<<<<< HEAD:tests/Rise_Tests.md
6. **Screenshots Comparasion:**  
   Successfully completing these steps and comparing the three screenshots without any discrepancies confirms that RISE is functioning effectively within the Jupyter Lab environment.
   ![Screenshot 2023-11-27 at 16 43 12](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/d703435e-541e-469a-b75c-45de0109f806)

7. **Enhanced RISE Testing with Sample Slides:**
=======
   Successfully completing these steps and comparing the three screenshots without any discrepancies confirms that RISE is functioning  effectively within the Jupyter Lab environment.
![Screenshot 2023-11-27 at 16 43 12](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/d703435e-541e-469a-b75c-45de0109f806)
   
7.** Enhanced RISE Testing with Sample Slides  **

Generate sample slides containing text, images, and notes, separated by dividing lines through scripts. Utilize Selenium to automate the opening of these slides and their conversion into a slideshow format. Then, capture screenshots of the slideshow for comparison against predefined slide templates to assess the visual effects.

![new_nb_screenshot 8](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/fbcb0e1f-7386-4a28-a845-3ed87bac0b31)
Sample notebook slides

![rise_screenshot 8](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/112d0594-2c81-4b01-ac23-f2e48f6a5bf6)
Sample slideshow

![Screenshot 2023-11-27 at 14 25 47](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/224279d2-584f-425f-971b-cf619fdf6595)


>>>>>>> origin/container-base-ope:tests/rise-test.md

   Generate sample slides containing text, images, and notes, separated by dividing lines through scripts. Utilize Selenium to automate the opening of these slides and their conversion into a slideshow format. Then, capture screenshots of the slideshow for comparison against predefined slide templates to assess the visual effects.

   ![new_nb_screenshot 8](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/fbcb0e1f-7386-4a28-a845-3ed87bac0b31)
   _Sample notebook slides_

   ![rise_screenshot 8](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/112d0594-2c81-4b01-ac23-f2e48f6a5bf6)
   _Sample slideshow_

   ![Screenshot 2023-11-27 at 14 25 47](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/224279d2-584f-425f-971b-cf619fdf6595)
