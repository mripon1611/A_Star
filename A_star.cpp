#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pi;
int main()
{
    int i,j,n,r,c,rc,sr,sc,tr,tc,n_obs,k,tmp,dis,tmp2,tmp3;
    int parent[200];

    char grid[100][100];
    cout<<"Enter grid size :\t";
    cin>>n;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            grid[i][j]='\0';
        }
    }
    cout<<"enter starting position (row,col):\n";
    cin>>sr>>sc;
    grid[sr][sc]='s';
    cout<<"enter target position (row,col):\n";
    cin>>tr>>tc;
    cout<<"No of obstacle (?):\t";
    cin>>n_obs;
    if(n_obs>0)
    {
        for(i=0;i<n_obs;i++)
        {
            cout<<"\nObstacle :\t"<<i+1<<endl;
            cin>>r>>c;
            grid[r][c]='#';
        }
    }
    rc=(sr*10)+sc;
    priority_queue<pi, vector<pi>, greater<pi> >  frontier;
    frontier.push(make_pair(0, rc));
    while (frontier.empty() == false)
    {
        pair<int, int> top = frontier.top();
        rc=top.second;
        i=rc/10;
        j=rc%10;

        frontier.pop();

        if((j+1)<n)
        {
            if((grid[i][j+1]!='_')&&(grid[i][j+1]!='#')&&(grid[i][j+1]!='s'))
            {
                grid[i][j+1]='_';
                tmp=(i*10)+(j+1);
                dis=(abs(sr-i)+abs(sc-(j+1)))+(abs(tr-i)+abs(tc-(j+1)));
                frontier.push(make_pair(dis,tmp));
                parent[tmp]=((i*10)+j);
            }
        }

        if((i-1)>=0)
        {
            if((grid[i-1][j]!='_')&&(grid[i-1][j]!='#')&&(grid[i-1][j]!='s'))
            {
                grid[i-1][j]='_';
                tmp=((i-1)*10)+j;
                dis=(abs(sr-(i-1))+abs(sc-j))+(abs(tr-(i-1))+abs(tc-j));
                frontier.push(make_pair(dis,tmp));
                parent[tmp]=((i*10)+j);
            }
        }

        if((j-1)>=0)
        {
            if((grid[i][j-1]!='_')&&(grid[i][j-1]!='#')&&(grid[i][j-1]!='s'))
            {

                grid[i][j-1]='_';
                tmp=(i*10)+(j-1);
                dis=(abs(sr-i)+abs(sc-(j-1)))+(abs(tr-i)+abs(tc-(j-1)));
                frontier.push(make_pair(dis,tmp));
                parent[tmp]=((i*10)+j);
            }
        }

        if((i+1)<n)
        {
            if((grid[i+1][j]!='_')&&(grid[i+1][j]!='#')&&(grid[i+1][j]!='s'))
            {
                grid[i+1][j]='_';
                tmp=((i+1)*10)+j;
                dis=(abs(sr-(i+1))+abs(sc-j))+(abs(tr-(i+1))+abs(tc-j));
                frontier.push(make_pair(dis,tmp));
                parent[tmp]=((i*10)+j);

            }
        }

    }

    grid[tr][tc]='t';
    tmp2=parent[(tr*10)+tc];
    tmp3=(sr*10)+sc;
    while(tmp2!=tmp3)
    {
        int k=tmp2;
        i=tmp2/10;
        j=tmp2%10;
        grid[i][j]='p';
        tmp2=parent[k];

    }

    cout<<endl<<endl<<"Final Grid :\n-----------------"<<endl;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            cout<<grid[i][j]<<"\t";
        }
        cout<<endl;
    }

    return 0;
}

