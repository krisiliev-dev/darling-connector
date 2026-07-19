# Model bake-off: same product, different models, separate result files.
$py = 'C:\Users\lora_\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe'
$runner = 'C:\Users\lora_\Desktop\product-review\agent-pipeline\run_one.py'
$dir = 'C:\Users\lora_\Desktop\product-review\agent-pipeline\bakeoff'
New-Item -ItemType Directory -Force $dir | Out-Null
$env:PIPELINE_NO_LESSONS = '1'

$candidates = @(
    @{ name = 'glm-4.7-flash';      model = 'glm-4.7-flash';                                   provider = 'zai' },
    @{ name = 'deepseek-v4-flash';  model = 'deepseek-ai/deepseek-v4-flash';                   provider = 'nvidia' },
    @{ name = 'mistral-large-3';    model = 'mistralai/mistral-large-3-675b-instruct-2512';    provider = 'nvidia' },
    @{ name = 'gemini-3.5-flash';   model = 'gemini-3.5-flash';                                provider = 'gemini' },
    @{ name = 'mistral-api-large';  model = 'mistral-large-latest';                            provider = 'custom:mistral' }
)

foreach ($c in $candidates) {
    Write-Output ('=== ' + $c.name + ' ===')
    $env:PIPELINE_MODEL = $c.model
    $env:PIPELINE_PROVIDER = $c.provider
    $env:PIPELINE_RESULTS_PATH = Join-Path $dir ($c.name + '.jsonl')
    & $py $runner '0151260'
    Write-Output ('exit: ' + $LASTEXITCODE)
}
