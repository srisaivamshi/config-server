CONFIG_SERVER_URL=http://localhost:6087/monitor  # Replace with your Config Server URL
BRANCH_TO_MONITOR=main  # Specify the branch to trigger the notification

# Check if the pushed branch matches the specified branch
while read oldrev newrev refname
do
    if [[ $refname == "refs/heads/$BRANCH_TO_MONITOR" ]]
    then
        curl -X POST $CONFIG_SERVER_URL -d "trigger=refresh"
    fi
done