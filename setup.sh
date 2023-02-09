Mkdir -p ~/.streamlit/

Echo "\
[server]\n\
headless = true\n\
Port = $PORT\n\
enableCORS=false\n\
\n\
" >  ~/.streamlit/config.toml

