# ReplicationPackage
The replication package for our article _The State of Serverless Applications: Collection,Characterization, and Community Consensus_ provides everything required to reproduce all results for the following three studies:
* [Serverless Application Collection](#Serverless-Application-Collection)
* [Serverless Application Characterization](#Serverless-Application-Characterization)
* [Comparison Study](#Comparison-Study)

## Serverless Application Collection
We  collect  descriptions  of  serverless  applications  from open-source  projects,  academic  literature,  industrial  literature, and scientific computing. 
### Open-source Applications
As a starting point, we used an existing data set on open-source serverless projects from [this study](https://gupea.ub.gu.se/bitstream/2077/62544/1/gupea_2077_62544_1.pdf). We removed small and inactive projects based on the number of files, commits, contributors, and watchers. Next, we manually filtered the resulting data set to include only projects that implement serverless applications. We provide [a table](Serverless%20Application%20Collection/Open%20source%20filtering.xlsx) containing all projects that remained after the filtering alongside the notes from the manualy filtering.
<p>
<img src="https://github.com/ServerlessApplications/ReplicationPackage/raw/main/images/OpenSourceFiltering.png?raw=true" width="1024">
</p>


### Academic Literature Applications
We based our search on an [existing community-curated dataset](https://doi.org/10.5281/zenodo.1175423) on literature for serverless computing consisting of over 180 peer-reviewed articles. First, we filtered the articles based on title and abstract. In a second iteration, we filtered out any articles that implement only a single function for evaluation purposes or do not include sufficient detail to enable a review. As the authors were familiar with some additional publications describing serverless applications, we contributed them to the community-curated dataset and included them in this study. We provide [a table](Serverless%20Application%20Collection/Academic%20literature%20filtering.xlsx) with our notes from the manual filtering.
<p>
<img src="https://github.com/ServerlessApplications/ReplicationPackage/raw/main/images/AcademicLiteratureFiltering.png?raw=true" width="1024">
</p>


### Scientific Computing Applications
Most of these scientifc computing serverless applications are still at an early stage and therefore there is little public data available. One of the authors is employed at the German Aerospace Center~(DLR) at the time of writing, which allowed us to collect information about several projects at DLR that are either currently moving to serverless solutions or are planning to do so. Additionally, an application from the German Electron Syncrotron~(DESY) could be included. For each of these scientifc computing applications, we provide a document containing a description of the project and the names our contacts that provided information for the characterization of these applications.

* [SC1 Copernicus Sentinel-1 for near-real time water monitoring](Serverless%20Application%20Collection/SC1%20Copernicus%20Sentinel-1.pdf)
* [SC2 Reprocessing Sentinel 5 Precursor data with ProEO](Serverless%20Application%20Collection/SC2%20Reprocesssing%20Sentinel%205%20Precursor%20Data%20with%20ProsEO.pdf)
* [SC3 High Performance Data Analytics for Earth Observation](Serverless%20Application%20Collection/SC3%20High%20Performance%20Data%20Analytic%20for%20Earth%20Observation.pdf)
* [SC4 Tandem-L exploitation platform](Serverless%20Application%20Collection/SC4%20Tandem-L%20exploitation%20platform.pdf)
* [SC5 Global Urban Footprint](Serverless%20Application%20Collection/SC5%20Global%20Urban%20Footprint.pdf)
* [SC6 DESY - High Throughput Data Taking](Serverless%20Application%20Collection/SC6%20DESY%20-%20High%20Throughput%20Data%20Taking.pdf)

### Collection of serverless applications
Based on the previously described methodology, we collected a diverse dataset of 89 serverless applications from open-source projects, academic literature, industrial literature, and scientific computing. This dataset is can be found [here](Serverless%20Application%20Characterization/Dataset.xlsx).


## Serverless Application Characterization

### Initial Ratings & Interrater Agreement Calculation
* Initial Ratings [a relative link](Serverless%20Application%20Characterization/Initial%20Characterizations.csv)
<p>
<img src="https://github.com/ServerlessApplications/ReplicationPackage/raw/main/images/InitialCharacterization.png?raw=true" width="1024">
</p>

* Scripts for overlapp [a relative link](Serverless%20Application%20Characterization/CalculateKappa.py)

### Final Dataset & Figure Generation
* Final dataset [a relative link](Serverless%20Application%20Characterization/Dataset.xlsx)

<p>
<img src="https://github.com/ServerlessApplications/ReplicationPackage/raw/main/images/Dataset.png?raw=true" width="1024">
</p>

* Scripts for figures [a relative link](Serverless%20Application%20Characterization/GenerateFigures.py)

### Results Including Unknown Data 
* Results including unknowns [a relative link](Serverless%20Application%20Characterization/CharacteristicsIncludingUnknown) + script [a relative link](Serverless%20Application%20Characterization/GenerateResultsIncludingUnknown.py)

<p>
<img src="https://github.com/ServerlessApplications/ReplicationPackage/raw/main/images/CharacteristicsIncludingUnknown.png?raw=true" width="400">
</p>


## Comparison Study
* Literature search results [a relative link](Comparison%20Study/ComparisonSearch.xlsx)

<p>
<img src="https://github.com/ServerlessApplications/ReplicationPackage/raw/main/images/ComparisonSearch.png?raw=true" width="1024">
</p>


* Mappings  [a relative link](Comparison%20Study/Comparison%20Mappings.xlsx)

<p>
<img src="https://github.com/ServerlessApplications/ReplicationPackage/raw/main/images/ComparisonMapping.png?raw=true" width="400">
</p>


* Scripts for comparison score [a relative link](Comparison%20Study/corroboration_analysis.py)

* Script for comparison figures [a relative link](Comparison%20Study/barcharts.py)
