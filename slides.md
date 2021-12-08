---
marp: true
title: GPCR drugs - a survey
theme: default
---

<style>
table {
    height: 100%;
    width: 100%;
    font-size: 30px;
    color: black;
}
th {
    color: blue;
}
</style>

# Drugs data

* To examine the link between mutational constraint and GPCR drug targets, we need to obtain high-quality annotations of GPCR drug targets
* For each GPCR, we'd like to know:
    * What drugs target it (Split GPCRs into targets & non-targets)
    * What the mode-of-action is 
    * What their indication class is 

---

# Drug-target links
* Many GPCR drugs (e.g. atypical antipsychotics) show polypharmacology
* Congreve et al (2019) - possibly too conservative, only includes a few targets
* Drugbank - possibly too liberal, includes many off-target binding affinities
* Ideally would only choose receptors which are intended targets. 
* As a compromise, include only targets at which drug has known functional effect

---

# Mode of action count and assignments

MOA | Count
--------|-----
antagonist | 985 | inactivating
agonist    | 558 | activating
binder     | 100 | unknown
partial agonist  | 55 | activating
inhibitor   |               52
ligand                          |              41
other/unknown                    |             23


---

# Drug mode-of-action and indication
* Some indications avaiable through OpenTargets
* Some available through WHO ATC
* Combine both of these as data probably incomplete