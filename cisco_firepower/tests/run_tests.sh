#!/usr/bin/env bash
remove_dir_and_file_type()
{
    newFile=$@
    newFile=${newFile/good_tests\/}
    newFile=${newFile/.json}
}


create_action_with_connection()
{
    printf "Adding connection details to all actions."
    for i in good_tests/*;
        do printf "\n---${i}---\n"
        printf "Running jq to add connection details.\n"
        remove_dir_and_file_type ${i}
        newFile="./tests_with_conn/${newFile}_connection.json"
        jq -s '.[0] * .[1]' ${i} connection.json > $newFile
    done
}


add_scan_results_to_bulk()
{
    for i in tests_with_conn/*;
        do
        file="./${i}"
        if [[ ${file} == *"bulk_add_scan_result_connection.json"* ]]; then
            printf "Running jq to add scan results.\n"
            tempFile="${file}.tmp"
            jq -s '.[0] * .[1]' ${file} scan_results.json > ${tempFile}
	    mv ${tempFile} ${file}
        fi
    done
}


execute_test()
{
    for i in tests_with_conn/*;
        do printf "\n---${i}---\n"
	printf "Running Action's test.\n"
        ../cisco_firepower-run --debug test < $i | jq '.'
    done
}


execute_run()
{
    for i in tests_with_conn/*;
        do printf "\n---${i}---\n"
	printf "Running Action's run.\n"
        ../cisco_firepower-run --debug run < $i | jq '.'
    done
}


cleanup()
{
    rm scan_results.json
    rm -rf tests_with_conn
}

python3 bulk_add_scan_result_generator.py --results 5000
mkdir -p tests_with_conn
create_action_with_connection
add_scan_results_to_bulk
{
    execute_test
} > output_test.txt 2>&1

{
    execute_run
} > output_run.txt 2>&1
cleanup
