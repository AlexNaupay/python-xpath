$text = "The text you are desperate to analyze :)";

$html = file_get_contents('/home/alexh/PycharmProjects/xpath/validation.html');

$process = new Process("python /home/alexh/PycharmProjects/xpath/validationphp.py '{$html}'");
$process->run();

// executes after the command finishes
if (!$process->isSuccessful()) {
    throw new ProcessFailedException($process);
}

dd($process->getOutput());