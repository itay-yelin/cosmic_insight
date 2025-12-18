param(
    [Parameter(Mandatory)]
    [ValidateSet("fmt","lint","type","test","all")]
    [string]$Task
)

switch ($Task) {
    "fmt"  { ruff format . }
    "lint" { ruff check . }
    "type" { mypy src }
    "test" { pytest }
    "all"  {
        ruff format .
        ruff check .
        mypy src
        pytest
    }
}
