/*
Write a function to find the longest common prefix string amongst an array of strings.
*/

char* longestCommonPrefix(char** strs, int strsSize) {
    int cur=0;
    if (strsSize<=0){
        return "";
    }
    if(strsSize==1){
        return strs[0];
    }
     char *ps=&strs[0][0];
    char *pr=(char*)calloc(1+strlen(strs[0]),sizeof(char));
    if (!pr){
        return -1;
    }
    while(*ps){
         for (int i=1;i<strsSize; i++){
            if (strs[i][cur]=='\0' || (strs[i][cur]!=*ps)){
                return pr;
            }
         }
         pr[cur]=*ps;
         ps++;
         cur++;
    }
    
    return pr;
    
}
