async function fetchData() {
        try {
            const username = "cuardido"

            let followers = [];
            let followings = [];
            let dontFollowMeBack = [];
            let iDontFollowBack = [];

            console.log(`Process started! Give it a couple of seconds`);

            const userQueryRes = await fetch(
            `https://www.instagram.com/web/search/topsearch/?query=${username}`
            );

            const userQueryJson = await userQueryRes.json();

            const userId = userQueryJson.users[0].user.pk;

            let after = null;
            let has_next = true;

            while (has_next) {
            await fetch(
                `https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables=` +
                encodeURIComponent(
                    JSON.stringify({
                    id: userId,
                    include_reel: true,
                    fetch_mutual: true,
                    first: 50,
                    after: after,
                    })
                )
            )
                .then((res) => res.json())
                .then((res) => {
                has_next = res.data.user.edge_followed_by.page_info.has_next_page;
                after = res.data.user.edge_followed_by.page_info.end_cursor;
                followers = followers.concat(
                    res.data.user.edge_followed_by.edges.map(({ node }) => {
                    return {
                        username: node.username,
                        full_name: node.full_name,
                    };
                    })
                );
                });
            }

            console.log({ followers });

            after = null;
            has_next = true;

            while (has_next) {
            await fetch(
                `https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables=` +
                encodeURIComponent(
                    JSON.stringify({
                    id: userId,
                    include_reel: true,
                    fetch_mutual: true,
                    first: 50,
                    after: after,
                    })
                )
            )
                .then((res) => res.json())
                .then((res) => {
                has_next = res.data.user.edge_follow.page_info.has_next_page;
                after = res.data.user.edge_follow.page_info.end_cursor;
                followings = followings.concat(
                    res.data.user.edge_follow.edges.map(({ node }) => {
                    return {
                        username: node.username,
                        full_name: node.full_name,
                    };
                    })
                );
                });
            }

            console.log({ followings });

            dontFollowMeBack = followings.filter((following) => {
            return !followers.find(
                (follower) => follower.username === following.username
            );
            });

            console.log({ dontFollowMeBack });

            iDontFollowBack = followers.filter((follower) => {
            return !followings.find(
                (following) => following.username === follower.username
            );
            });

            console.log({ iDontFollowBack });

            followers = ordenarPorNome(followers);
            followings = ordenarPorNome(followings);
            dontFollowMeBack = ordenarPorNome(dontFollowMeBack);
            iDontFollowBack = ordenarPorNome(iDontFollowBack);

    
            return {
                followers,
                followings,
                dontFollowMeBack,
                iDontFollowBack,
            };
        } catch (err) {
            console.log({ err });
        }
}

function ordenarPorNome(array) {
    return array.sort(function (a, b) {
        if (a.username > b.username) {
            return 1;
        }
        if (a.username < b.username) {
            return -1;

        }
        return 0;
    });
}



// Função para salvar conteúdo em um arquivo
function download(content, filename) {
    const element = document.createElement('a');
    element.href = URL.createObjectURL(new Blob([content], { type: 'text/plain' }));
    element.download = filename;
    document.body.appendChild(element);
    element.click();
}

// As variáveis que você deseja salvar
const dataToSave = {
    data : await fetchData()
};
    
// Converter as variáveis em formato JSON
const jsonData = JSON.stringify(dataToSave, null, 2);

// Salvar o conteúdo em um arquivo
download(jsonData, 'data.json');