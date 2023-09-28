aws sts get-caller-identity > /dev/null
creds=$(curl -s ${IAM_HOST}/latest/meta-data/iam/security-credentials/${IAM_ROLE})
IFS=$'\n' lines=($creds)
for line in "${lines[@]}"; do
  echo "::add-mask::$line"
done
export AWS_ACCESS_KEY_ID=$(echo $creds | jq -r .AccessKeyId)
echo "::add-mask::$AWS_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY=$(echo $creds | jq -r .SecretAccessKey)
echo "::add-mask::$AWS_SECRET_ACCESS_KEY"
export AWS_SESSION_TOKEN=$(echo $creds | jq -r .Token)
echo "::add-mask::$AWS_SESSION_TOKEN"