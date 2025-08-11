# titanic
### **1. Age Distribution**

* Most passengers were between **20–40 years old**.
* There’s a slight peak for children, suggesting some families onboard.
* Age distribution is right-skewed, meaning there are fewer older passengers.

---

### **2. Overall Survival Rate**

* More passengers **did not survive** than survived (approx. 62% vs. 38% from the countplot).
* This confirms the Titanic disaster had a high fatality rate.

---

### **3. Survival by Sex**

* **Females** had a much higher survival rate than males.
* This matches the historical “**women and children first**” evacuation approach.
* Most male passengers did not survive.

---

### **4. Correlation Heatmap**

* `Sex` (encoded) has a strong negative correlation with `Survived` → meaning being female is positively associated with survival.
* `Pclass` shows a negative correlation → lower class number (1st class) tends to survive more.
* `Fare` shows a positive correlation → higher ticket price is associated with higher survival chances.

---

### **5. Missing Values Handling**

* Age and Embarked were successfully imputed without losing important data.
* Dropping `Cabin` was reasonable since too many values were missing.

---

✅ **Overall Conclusion:**
Survival chances were strongly influenced by **gender, passenger class, and fare paid**. Women, passengers in higher classes, and those who paid higher fares had a better chance of survival. Age played a role, but less strongly than sex and class.

---
