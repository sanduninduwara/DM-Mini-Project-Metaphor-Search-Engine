# DM-Mini-Project-Metaphor-Search-Engine-



## Step 1: Install Elasticsearch and Disable Security Features

## Step 2: Setup Elasticsearch Indices and Import Data

### Go to the path dataset
Navigate to the dataset directory and create an Elasticsearch index for poems. Import data into the Elasticsearch index using appropriate JSON files.

#### Create Elasticsearch index by running
curl -X PUT "localhost:9200/poems?pretty" -H "Content-Type: application/json" -d @mapping_file.json

#### Import data into Elasticsearch index by running
curl -X POST "localhost:9200/poems/_bulk?pretty" -H "Content-Type: application/json" --data-binary @data_file.json

## Step 3: Install Required Python Libraries
pip install -r requirements.txt

## Step 4: Run the Application
python main.py
