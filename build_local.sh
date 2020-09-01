yarn build

mkdir -p build/root
for file in $(ls build | grep -E -v '^(index\.html|static|root)$'); do
    mv "build/$file" build/root;
done

python3 -m pipenv run python ./manage.py collectstatic --no-input
